import json
import httpx
import ssl
import tempfile
from django.conf import settings

class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.ssl_context = self._create_ssl_context()

    def _create_ssl_context(self):
        # Создаём временные файлы для сертификата и ключа
        with tempfile.NamedTemporaryFile(delete=False) as cert_file, \
             tempfile.NamedTemporaryFile(delete=False) as key_file:
            cert_file.write(settings.TLS_CERT.encode())
            key_file.write(settings.TLS_KEY.encode())
            cert_file.flush()
            key_file.flush()

            # Создаём SSL-контекст и загружаем временные файлы
            ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ssl_context.load_cert_chain(cert_file.name, keyfile=key_file.name)
        
        return ssl_context

    def call_method(self, method, params=None):
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1
        }

        try:
            with httpx.Client(verify=self.ssl_context) as client:
                response = client.post(
                    self.endpoint,
                    json=payload,
                    headers=headers
                )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            return {"error": str(e)}