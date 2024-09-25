class Solution():
    def isPalindrome(self, x):
        if x < 0:
            return False

        stringx = str(x)

        return stringx == stringx[::-1] # Formula for palindrome

obj = Solution()
y = int(input("Number: "))
print(f"Palindrome? : {obj.isPalindrome(y)}")

#How in the world did somone manage to run it in only 7 Ms? Maybe used different language.