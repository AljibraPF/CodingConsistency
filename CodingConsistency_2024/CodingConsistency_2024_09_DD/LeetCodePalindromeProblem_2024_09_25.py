class Solution():
    def isPalindrome(self, x):
        if x < 0:
            return False

        stringx = str(x)

        return stringx == stringx[::-1]

