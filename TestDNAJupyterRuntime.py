import unittest

class TestDNAJupyterRuntime(unittest.TestCase):

    def test_userkey(self):
        self.assertEqual(len(self), 32)


if __name__ == '__main__':
    unittest.main()