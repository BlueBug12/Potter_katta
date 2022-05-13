import unittest
from Potter import Potter
book_price = 8
class TestPotter(unittest.TestCase):
    def setUp(self):
        self.test_object = Potter(book_price)
    def testBasics(self):
        assert (0 == self.test_object.price([]))
        assert (book_price == self.test_object.price([1]))
        assert (book_price == self.test_object.price([2]))
        assert (book_price == self.test_object.price([3]))
        assert (book_price == self.test_object.price([4]))
        assert (book_price * 3 == self.test_object.price([1, 1, 1]))
    def testSimpleDiscounts1(self):
        assert (book_price * 2 * 0.95 == self.test_object.price([0, 1]))
    def testSimpleDiscounts2(self):
        assert (book_price * 3 * 0.9 == self.test_object.price([0, 2, 4]))
    def testSimpleDiscounts3(self):
        assert (book_price * 4 * 0.8 == self.test_object.price([0, 1, 2, 4]))
    def testSimpleDiscounts4(self):
        assert (book_price * 5 * 0.75 == self.test_object.price([0, 1, 2, 3, 4]))
    def testSeveralDiscounts(self):
        assert (book_price + (book_price * 2 * 0.95) == self.test_object.price([0, 0, 1]))
        assert (2 * (book_price * 2 * 0.95) == self.test_object.price([0, 0, 1, 1]))
        assert ((book_price * 4 * 0.8) + (book_price * 2 * 0.95) == self.test_object.price([0, 0, 1, 2, 2, 3]))
        assert (book_price + (book_price * 5 * 0.75) == self.test_object.price([0, 1, 1, 2, 3, 4]))
        assert (2 * 4 * book_price * 0.8 == self.test_object.price([0, 0, 1, 1, 2, 2, 3, 4]))
if __name__ == '__main__':
    unittest.main()
