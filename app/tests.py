from django.test import TestCase
from django.urls import reverse
from django.conf import settings
import json
from app.utils.web_client import JsonRpcClient  # Импортируем твой клиент


class RpcCallTestCase(TestCase):

    def setUp(self):
        # Указываем URL, который будет использоваться для RPC вызовов
        self.endpoint = settings.JSONRPC_ENDPOINT
        self.client = JsonRpcClient(self.endpoint)

    def test_auth_check(self):
        # Параметры для вызова
        method = "auth.check"
        params = {"user_id": 1192}

        # Отправляем RPC запрос через свой клиент
        response = self.client.call_method(method, params)

        # Проверка успешного ответа
        self.assertIn("jsonrpc", response)
        self.assertEqual(response["jsonrpc"], "2.0")
        self.assertIn("result", response)

    def test_fake_methods(self):
        # Список фальшивых методов
        data_list = [
            {"method": "auth.fake", "params": None},
            {"method": "auth.more_fake", "params": None},
            {"method": "auth.111", "params": None},
        ]

        for data in data_list:
            response = self.client.call_method(data["method"], data["params"])
            print(response)  # Выводим содержимое ответа

            # Проверка, что ошибка присутствует в ответе
            self.assertIn("error", response)
            self.assertNotEqual(response.get("error"), None)
