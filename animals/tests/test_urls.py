from django.test import TestCase, RequestFactory
from animals.views import index


class AnimalsUrlsTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_route_url_used_view_index(self):
        """" Teste se a home da aplicaçõo utiliza a função indez da  view"""
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)

