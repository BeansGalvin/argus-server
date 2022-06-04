import unittest
from src.ServerRoot import application


class TestRecordSighting(unittest.TestCase):

    def setUp(self):
        self.app = application

    def tearDown(self):
        self.app = None

    def testWriteSighting(self):  # must be prefixed with 'test...'
        self.app is not None
        self.assertTrue(False)
