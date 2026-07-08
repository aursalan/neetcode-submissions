class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        clean_nums = set(nums)
        length = 0
        for i in clean_nums:
            temp_length = 0
            for j in range(i, max(nums)+1):
                if j in clean_nums:
                    temp_length+=1
                    if temp_length>length:
                        length = temp_length
                else:
                    break
                            
        return length
