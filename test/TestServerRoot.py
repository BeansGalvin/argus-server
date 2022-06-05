from starlettce.testclient import TestClient
import unittest
from src.ServerRoot import application


class TestServerRoot(unittest.TestCase, TestClient):
    client = TestClient(application)

    def test_server_running(self):  # must be prefixed with 'test...'
        self.assertIsNotNone(self.client)
        response = self.client.get("/")
        print('response is:') #debug
        print(response.json()) #debug
        self.assertEqual(response.status_code, 200)

    def test_responses(self):  # must be prefixed with 'test...'
        self.assertIsNotNone(application)
        response = self.client.get("/")
        self.assertEqual(response.json(), {'message': 'Hello World'})