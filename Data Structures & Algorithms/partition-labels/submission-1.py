class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}

        for i, char in enumerate(s):
            last[char]=i
        
        result = []
        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, last[char])

            if end == i:
                result.append(i - start + 1)
                start = i + 1
        
        return result
