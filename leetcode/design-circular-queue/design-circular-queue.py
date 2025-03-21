from typing import List

# optimal solution
# Time O() | Space O()
# In this problem,

class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1]*k
        self.head = 0
        self.tail = -1
        self.capacity = k
        self.length = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail += 1
            self.tail %= self.length
            self.arr[self.tail] = value
            self.capacity -= 1
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head += 1
            self.head %= self.length
            self.capacity += 1
            return True
        return False

    def Front(self) -> int:
        if self.head >= 0:
            return self.arr[self.head]
        return -1

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        if self.tail >= 0:
            return self.arr[self.tail]
        return -1

    def isEmpty(self) -> bool:
        if self.capacity == len(self.arr):
            return True
        return False

    def isFull(self) -> bool:
        if self.capacity == 0:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(7))
print(myCircularQueue.deQueue())
print(myCircularQueue.Front())
print(myCircularQueue.deQueue())
print(myCircularQueue.Front())
print(myCircularQueue.Rear())
print(myCircularQueue.enQueue(0))
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.Rear())
print(myCircularQueue.enQueue(3))
## 
        # print(nums)
# arr = [2, 7, 11, 15]
# k = Solution().method_template(arr)
# print(k)
        
# https://leetcode.com/problems/design-circular-queue/
