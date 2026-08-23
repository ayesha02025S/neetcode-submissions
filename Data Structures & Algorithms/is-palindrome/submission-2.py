class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = ''
        for c in s:
            if c.isalnum():
                cleanString += c.lower()
        return cleanString == cleanString[::-1]
        