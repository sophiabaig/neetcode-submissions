class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:

            alpha_word = ''.join(sorted(word.lower()))

            if alpha_word not in anagrams:
                anagrams[alpha_word] = []

            anagrams[alpha_word].append(word)
        
        result = []

        for key, value in anagrams.items():
            result.append(value)
    
        return result