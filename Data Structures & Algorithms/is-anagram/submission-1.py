class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        counts_s = {}
        counts_t = {}

        for x in s:
            if x in counts_s:
                counts_s[x]+=1
            else:
                counts_s[x]=1
        
        for x in t:
            if x in counts_t:
                counts_t[x]+=1
            else:
                counts_t[x]=1
        
        return counts_s==counts_t