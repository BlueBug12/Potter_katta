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
        if len(basket) == 0:
            return 0
        elif len(basket) == 1:
            return 8
        elif len(basket) == 2:
            return 8*2*0.95
        elif len(basket) == 3:
            return 8*3*0.9
        elif len(basket) == 4:
            return 8*4*0.8
        else:
            return 8*5*0.75
        
