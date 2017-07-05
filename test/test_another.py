import unittest

__author__ = 'brouk'


class TestSomething(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.t = True
        self.f = False
        self.value = 25

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_default_values(self):
        self.assertTrue(self.t, msg='Member variable "t" is not "True" !')
        self.assertFalse(self.f, msg='Member variable "f" is not "False" !')
        self.assertEquals(self.value, 25, msg='Member variable "value" is not "25" !')

if __name__ == '__main__':
    unittest.main()
