class ProductOfNumbers:
    # We can keep track of the total product of the stream
    # We can keep track of the product up to and including the last character from the start of the stream
    # During add, add a new entry to the list of products
    # During getProduct divide total by the product up to a specific value
    # for 0s, exclude them from the total product
    # and keep track of the latest 0 in the stream because any product before that will be 0
    def __init__(self):
        self.latest_zero = -1
        self.total_products = [1]
        self.elem_total = 0

    def add(self, num: int) -> None:
        self.elem_total += 1
        if num == 0:
            self.latest_zero = self.elem_total
            self.total_products.append(self.total_products[-1])
            return
        self.total_products.append(self.total_products[-1] * num)

    def getProduct(self, k: int) -> int:
        cutoff = self.elem_total - k
        if cutoff < self.latest_zero:
            return 0
        else: 
            return self.total_products[-1] // self.total_products[cutoff]
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
