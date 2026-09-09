class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        counts = {}
        max_len = 0

        for right in range(len(s)):

            if s[right] not in counts:
                counts[s[right]] = 0
            counts[s[right]] += 1

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left+=1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        

