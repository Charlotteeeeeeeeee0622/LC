from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            ind = (len(self.arr)) // 2
            return self.arr[ind]

        if len(self.arr) % 2 == 0:
            ind1 = len(self.arr) // 2
            ind2 = (len(self.arr) - 1) // 2
            return float(self.arr[ind1] + self.arr[ind2]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()