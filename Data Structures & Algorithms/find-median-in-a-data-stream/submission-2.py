import heapq 

class MedianFinder:

    def __init__(self):
        self.left_max, self.right_min = [], []

    def addNum(self, num: int) -> None:
        if self.right_min and num > self.right_min[0]:
            heapq.heappush(self.right_min, num)

        else:
            heapq.heappush(self.left_max, -num)

        if len(self.left_max) > len(self.right_min) + 1:
            value = -heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, value)

        if len(self.right_min) > len(self.left_max) + 1:
            value = -heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, value)


    def findMedian(self) -> float:
        if len(self.left_max) > len(self.right_min):
            return -self.left_max[0]

        elif len(self.right_min) > len(self.left_max):
            return self.right_min[0]

        else:
            return (-self.left_max[0] + self.right_min[0]) / 2.0
        

        