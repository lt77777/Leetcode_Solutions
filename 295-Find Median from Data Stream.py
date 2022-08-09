class MedianFinder:

    def __init__(self):
        
        self.array = []

    def addNum(self, num: int) -> None:
        
        self.array.append(num)

    def findMedian(self) -> float:
        
        self.array.sort()
        l = len(self.array)

        if l % 2 == 0:
            return (self.array[(l-1) // 2] + self.array[((l-1) // 2) + 1]) / 2
        elif l % 2 != 0:
            return self.array[(l - 1) // 2] 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
