class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_map = {}

        for s in strs:

            sorted_s = "".join(sorted(s))

            if sorted_s not in str_map:
                str_map[sorted_s] = []

            str_map[sorted_s].append(s)
        
        output = []

        for s, anagrams in str_map.items():

            output.append(anagrams)

        return output

