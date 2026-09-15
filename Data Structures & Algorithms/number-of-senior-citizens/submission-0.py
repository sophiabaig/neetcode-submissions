class Solution:
    def countSeniors(self, details: List[str]) -> int:

        numSeniors = 0

        for detail in details:

            if int(detail[11:13]) > 60:
                numSeniors+=1
            
        
        return numSeniors

        