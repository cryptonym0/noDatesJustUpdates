class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # take in k
        self.k = k
        self.stream = nums
        self.stream.sort(reverse=True)
        return None

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse=True)
        return self.stream[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# 3rd largest
# i=0: [8,5,4,2] k=3
# i=1: add(3) list: [8,5,4,3,2] k=3 rtn.append(4)
# i=1: add(5) list: [8,5,5,4,3,2] k=3 rtn.append(5)
# i=1: add(10) list: [10,8,5,5,4,3,2] k=3 rtn.append(5)
# i=1: add(9) list: [10,9,8,5,5,4,3,2] k=3 rtn.append(8)
# i=1: add(4) list: [10,9,8,5,5,4,4,3,2] k=3 rtn.append(8)
# return = null,4,5,5,8
# ok I got it
