class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        res = []
        for i in nums:
            if i in freqs:
                freqs[i]+=1
            else:
                freqs[i]=1
        
        buckets = {}
        for num, freq in freqs.items():
            if freq in buckets:
                buckets[freq].append(num)
            else:
                buckets[freq]=[num]
        
        buckets_index = sorted(buckets, reverse=True)
        
        # print(buckets, buckets_index)
        
        for i in buckets_index:
            if len(res)==k:
                break
            else:
                for j in buckets[i]:
                    if len(res)!=k:
                        res.append(j)

        return res
