import imp
import unittest
from Potter import Potter

class TestPotter(unittest.TestCase):
    def setUp(self):
        self.test_object = Potter()
    def testBasics(self):
        assert (0 == self.test_object.price([]))
        assert (8 == self.test_object.price([1]))
        assert (8 == self.test_object.price([2]))
        assert (8 == self.test_object.price([3]))
        assert (8 == self.test_object.price([4]))
        assert (8 * 3 == self.test_object.price([1, 1, 1]))
if __name__ == '__main__':
    unittest.main()
