class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict = {}

        for curr_s in strs:

            sorted_s = "".join(sorted(curr_s))

            if sorted_s in result_dict:
                result_dict[sorted_s].append(curr_s)
            else:
                result_dict[sorted_s] = []
                result_dict[sorted_s].append(curr_s)

        result = []
        for key, words in result_dict.items():
            result.append(words)
            
        return result




        