from django.test import TestCase
from django.urls import reverse

class RpcClientTests(TestCase):
    def test_page_loads(self):
        response = self.client.get(reverse('rpc_call'))
        self.assertEqual(response.status_code, 200)