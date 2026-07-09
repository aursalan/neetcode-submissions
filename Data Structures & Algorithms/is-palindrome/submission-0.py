class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        rep_s = []

        for char in s:
            unicode = ord(char)
            if 48 <= unicode <= 57 or 65 <= unicode <=90 or 97 <= unicode <= 122  :
                rep_s.append(char)

        s = "".join(rep_s)
    
        return True if s[::-1] == s else False