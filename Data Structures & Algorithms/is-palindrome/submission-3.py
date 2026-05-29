class Solution:
    # two pointers, one at the i = 0, one at i = len(s) - 1
    # increase l, decrease r, while l < r
    # check if they are equal, if not equal, return False
    # if exit loop return True
    # we should also lowercase the string, and 
    # remove all non-alphanumeric characters
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

        