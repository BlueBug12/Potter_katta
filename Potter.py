class Potter:
    def price(self, basket):
        max_combine = len(set(basket))
        if max_combine == len(basket):
            return self.discountprice(basket)
        else:
            return 8 * len(basket)
    def discountprice(self, basket):
        return 0
