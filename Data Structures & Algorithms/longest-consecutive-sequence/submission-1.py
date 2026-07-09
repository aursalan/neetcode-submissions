class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        clean_nums = set(nums)
        length = 0

        for i in clean_nums:

            temp_length = 0

            if i-1 in clean_nums:
                continue
            
            else:
                current = i
                while current in clean_nums:
                    print(current)
                    temp_length+=1
                    current+=1

            if temp_length>length:
                length = temp_length
                            
        return length
