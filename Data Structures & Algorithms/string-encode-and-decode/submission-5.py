class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            result+=str(len(word))
            result+="#"
            result+=word

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        length = ""
        i = 0

        while i < len(s):
            if s[i] != "#":
                length+=s[i]
                i+=1
            else:
                length=int(length)
                word=s[i+1:i+1+length]
                result.append(word)
                i=i+1+length
                length=""
             
        return result





        
