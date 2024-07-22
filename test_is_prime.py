import unittest
from is_prime import is_prime
class TryTesting(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)
    
    def test_fail(self):
        self.assertFalse(False)

    def test_isPrime(self):
        self.assertFalse(is_prime(20))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(None))
        self.assertFalse(is_prime(0))


if __name__ == '__main__':
    unittest.main()
        