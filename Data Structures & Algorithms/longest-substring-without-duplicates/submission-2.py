class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        for i in range(len(s)):

            seen = set()
            j = i
            while j<len(s):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    j+=1
            length = len(seen)
            if length>maxLength: 
                maxLength = len(seen)
                
        return maxLength