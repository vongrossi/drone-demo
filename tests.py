import unittest
from app import app


class TestHello(unittest.TestCase):
    def test_redis(self):
        app.testing = True

        val = app.test_client().get('/')
        self.assertIn('<b>Visits:</b> 1', val.data)

        val = app.test_client().get('/')
        self.assertIn('<b>Visits:</b> 2', val.data)


if __name__ == '__main__':
    unittest.main()
