class Potter:
    def __init__(self,book_price):
        self.book_price = book_price
        self.discount = {0:1, 1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
    def pick_combination(self, basket, books_num):
        return list(set(basket))[:books_num]
    def remove_books_from_basket(self, basket, books):
        for b in books:
            basket.remove(b)
        return basket
    def discountprice(self, basket):
        type_num = len(basket)
        if len(set(basket)) != type_num:
            print('Error: only accept unique basket.')
        return self.book_price*type_num*self.discount[type_num]
    def price(self, basket):
        if len(set(basket)) == len(basket):
            return self.discountprice(basket)
        else:
            max_combine = len(set(basket))
            comb = self.pick_combination(basket, max_combine)
            return self.discountprice(comb) + self.price(self.remove_books_from_basket(basket, comb))
        
