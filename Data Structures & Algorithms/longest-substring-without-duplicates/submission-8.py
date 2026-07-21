class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0,0
        maxLength = 0
        seen = set()

        while right<len(s):
                
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                maxLength = max(maxLength, len(seen))

            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1


                
        return maxLength