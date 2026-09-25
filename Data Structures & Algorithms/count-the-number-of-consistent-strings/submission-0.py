class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total_count = 0

        allowed_chars = set()
        for c in allowed:
            allowed_chars.add(c)

        for word in words:
            count = 0
            for c in word:
                if c not in allowed_chars:
                    break
                count += 1
            
            if count == len(word):
                total_count+=1
        
        return total_count