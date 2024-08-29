class Solution():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    
    def is_sum_equal(self):
        return self.left + self.right == self.val


Ins1 = Solution(5,4,2)
print(Ins1.is_sum_equal())

