import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []
        # Python heap is min heap here, 
        # so we add a minus sign to make it a max heap

    def addNum(self, num: int) -> None:
        # add item
        if len(self.minheap) > 0 and num > self.minheap[0]:
            # add to the min heap
            heapq.heappush(self.minheap, num)
        else:
            # add to the max heap, add a minus sign
            heapq.heappush(self.maxheap, -num)
        
        # check balance
        while len(self.maxheap) > len(self.minheap):
            # pop the maximum from the max heap
            item = -heapq.heappop(self.maxheap)
            # push it to the min heap, recover it from the minus sign
            heapq.heappush(self.minheap, item)
        while len(self.minheap) - 1 > len(self.maxheap):
            # pop the maximum from the min heap
            item = heapq.heappop(self.minheap)
            # push it to the max heap
            heapq.heappush(self.maxheap, item)

    def findMedian(self) -> float:
        # check if the number of elements is odd
        k = len(self.minheap) + len(self.maxheap)
        if k % 2 == 1:
            if len(self.minheap) > 0:
                # take the max from the max heap
                return self.minheap[0]
            else:
                return -self.maxheap[0]
        else:
            # take the max from the max heap
            max_item = -self.maxheap[0]
            # take the min from the min heap
            min_item = self.minheap[0]
            # return the average
            return (max_item + min_item) / 2



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())

# obj = MedianFinder()
# obj.addNum(1)
# print(obj.findMedian())

# obj = MedianFinder()
# obj.addNum(-1)
# print(obj.findMedian())
# obj.addNum(-2)
# print(obj.findMedian())
# obj.addNum(-3)
# print(obj.findMedian())
# obj.addNum(-4)
# print(obj.findMedian())
# obj.addNum(-5)
# print(obj.findMedian())
