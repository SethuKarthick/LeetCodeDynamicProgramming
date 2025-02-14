class ProductOfNumbers:

    def __init__(self):
        self.pref_prod = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.pref_prod = [1]
        else:
            self.pref_prod.append(self.pref_prod[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref_prod):
            return 0
        
        return self.pref_prod[-1] // self.pref_prod[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)