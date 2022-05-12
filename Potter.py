class Potter:
    def price(self, basket):
        max_combine = len(set(basket))
        if max_combine == len(basket):
            return self.discountprice(basket)
        else:
            return 8 * len(basket)
    def discountprice(self, basket):
        if len(set(basket)) != len(basket):
            print('Error: only accept unique basket.')
        discount = {0:1, 1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
        return 8*len(basket)*discount[len(basket)]
        
