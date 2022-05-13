from itertools import combinations
class Potter:
    def __init__(self,book_price):
        self.book_price = book_price
        self.discount = {0:0, 1:1, 2:1.9, 3:2.7, 4:3.2, 5:3.75}
    def remove_books_from_basket(self, basket, books):
        for b in books:
            basket.remove(b)
        return basket
    def discountprice(self, n):
        return self.book_price*self.discount[n]
    def price(self, basket):
        type_num = len(set(basket))
        return self.count(basket,type_num)

    def count(self,basket,num):
        type_list = list(set(basket))
        if len(type_list) == len(basket):
            return self.discountprice(len(type_list))
        if len(type_list) == 1:
            return len(basket)*self.book_price
        total_p = 1e9
        for j in range(num,0,-1):
            combs = combinations(type_list,j)
            for comb in combs:
                self.remove_books_from_basket(basket,comb)
                total_p = min(self.count(basket,j)+self.discountprice(j),total_p)
                basket += comb
        return total_p

if __name__ == "__main__":
    p = Potter(8)
    print(p.price([0,0,1,1]))
