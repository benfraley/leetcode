class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower()) # remove non alphanumerics
        return clean == clean[::-1] # compare the array to its reverse
        