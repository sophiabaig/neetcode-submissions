class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key: sorted word ; value: list of words
        anagrams = {} 
        
        for x in strs:
            sorted_word = "".join(sorted(x))

            if sorted_word in anagrams:
                # same anagram already in dict
                anagrams[sorted_word].append(x)
            else:
                anagrams[sorted_word]=[]
                anagrams[sorted_word].append(x)
        
        final_val = []
        for x in anagrams:
            final_val.append(anagrams[x])

        return final_val