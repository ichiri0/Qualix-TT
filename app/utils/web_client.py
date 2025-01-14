import json
import requests
from QualixTT import settings

class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.cert = (settings.TLS_CERT, settings.TLS_KEY)

    def call_method(self, method, params=None):
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1
        }
        try:
            response = requests.post(
                self.endpoint,
                data=json.dumps(payload),
                headers=headers,
                cert=self.cert,
                verify=True
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}