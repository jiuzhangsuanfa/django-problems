from django.test import TestCase


class AppTestCase(TestCase):

    def setUp(self):
        pass

    def should_startup(self):
        print('django startup succeed')
