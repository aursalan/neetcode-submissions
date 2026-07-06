class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            length = len(s)
            string = string + str(length) + "#" + s
        return string




    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        lastcharindex = 0
        i = 0
        while i<len(s) and lastcharindex<len(s):
            string = ""
            length = 0
            if s[i] == "#":
                length = int(s[lastcharindex:i])
                if length == 0:
                    lastcharindex = length+i+1
                    string = ""
                else:
                    lastcharindex = length+i+1
                    string = s[i+1:lastcharindex]
            
                res.append(string)

                i = lastcharindex+1
            else: 
                i+=1
        return res

