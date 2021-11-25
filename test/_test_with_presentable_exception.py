from django.http import request
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework.views import APIView
from presentable_exception.presentable_exception import PresentableClientException, PresentableServerException
from presentable_exception.with_presentable_exception import WithPresentableException
from test.fake_scenario import FakeScenario, FakeScenarioLoader
import json

class ClientsFaultView(WithPresentableException, APIView):
    
    def get(self, request):
        raise PresentableClientException(
            FakeScenario(
                package='package', 
                key='key', 
                message='a message', 
                log_entry={'log': 'entry'}, 
                responsible='client'))

class ServersFaultView(WithPresentableException, APIView):

    def get(self, request):
        raise PresentableServerException(
                FakeScenario(
                    package='package', 
                    key='key', 
                    message='a message', 
                    log_entry={'log': 'entry'}, 
                    responsible='server'))

class TestWithPresentableException(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/some/path')

    def test_clients_fault(self):
        response = ClientsFaultView().as_view()(self.request)
        self.assertEqual(400, response.status_code)
        self.assertEqual({'log': 'entry'}, response.data)

    def test_servers_fault(self):
        response = ServersFaultView().as_view()(self.request)
        self.assertEqual(500, response.status_code)
        self.assertEqual({'log': 'entry'}, response.data)