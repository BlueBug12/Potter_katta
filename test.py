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
    def testSimpleDiscounts1(self):
        assert (8 * 2 * 0.95 == self.test_object.price([0, 1]))
    def testSimpleDiscounts2(self):
        assert (8 * 3 * 0.9 == self.test_object.price([0, 2, 4]))
    def testSimpleDiscounts3(self):
        assert (8 * 4 * 0.8 == self.test_object.price([0, 1, 2, 4]))
    def testSimpleDiscounts4(self):
        assert (8 * 5 * 0.75 == self.test_object.price([0, 1, 2, 3, 4]))
    def testSeveralDiscounts(self):
        assert (8 + (8 * 2 * 0.95) == self.test_object.price([0, 0, 1]))
        assert (2 * (8 * 2 * 0.95) == self.test_object.price([0, 0, 1, 1]))
        assert ((8 * 4 * 0.8) + (8 * 2 * 0.95) == self.test_object.price([0, 0, 1, 2, 2, 3]))
        assert (8 + (8 * 5 * 0.75) == self.test_object.price([0, 1, 1, 2, 3, 4]))
if __name__ == '__main__':
    unittest.main()
