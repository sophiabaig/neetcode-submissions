class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_counts, s2_counts = {}, {}
        
        for i in range(len(s1)):
            if s1[i] not in s1_counts:
                s1_counts[s1[i]]=0
            if s2[i] not in s2_counts:
                s2_counts[s2[i]]=0
            s1_counts[s1[i]]+=1
            s2_counts[s2[i]]+=1
        
        if s1_counts == s2_counts:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            if s2[right] not in s2_counts:
                s2_counts[s2[right]]=0
            s2_counts[s2[right]]+=1
            s2_counts[s2[left]]-=1
            if s2_counts[s2[left]] == 0:
                del s2_counts[s2[left]]
            left+=1
            if s1_counts == s2_counts:
                return True
        return False


        