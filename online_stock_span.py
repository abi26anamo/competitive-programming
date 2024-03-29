class StockSpanner:

    def __init__(self):
        self.stock = []
        
    def next(self, price: int) -> int:
        count =1
        while self.stock and self.stock[-1][0]<=price:
            count+=self.stock.pop()[1]
        self.stock.append([price,count])
        return count
      
