class Potter:
    def pick_combination(self, basket, books_num):
        return list(set(basket))[:books_num]
    def remove_books_from_basket(self, basket, books):
        for b in books:
            basket.remove(b)
        return basket
    def discountprice(self, basket):
        if len(set(basket)) != len(basket):
            print('Error: only accept unique basket.')
        discount = {0:1, 1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
        return 8*len(basket)*discount[len(basket)]
    def price(self, basket):
        if len(set(basket)) == len(basket):
            return self.discountprice(basket)
        else:
            max_combine = len(set(basket))
            comb = self.pick_combination(basket, max_combine)
            return self.discountprice(comb) + self.price(self.remove_books_from_basket(basket, comb))
        
