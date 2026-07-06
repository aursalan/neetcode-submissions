from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = Counter(nums)
        bucket =[[] for i in range(len(nums)+1)]

        for num, frequency in frequencies.items():
            bucket[frequency].append(num)

        res = []

        for i in range(len(bucket)-1, 0, -1):
            if bucket[i] == []:
                continue
            for j in bucket[i]:
                if len(res)!=k:
                    res.append(j)
        
        return res

        