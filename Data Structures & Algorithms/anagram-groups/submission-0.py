class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            initial = [0]*26
            key = []
            
            for i in s:
                index = ord(i)-ord('a')
                initial[index]+=1
            
            key = tuple(initial)

            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)

        
        return list(res.values())



        