class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def isCorrect(passengerDetail: str) -> bool:
            if len(passengerDetail) != 15:
                return False
            
            if passengerDetail[10] not in { 'M', 'F', 'O' }:
                return False
            
            try:
                int(passengerDetail[:10])
                int(passengerDetail[11:])
            except:
                return False
            
            return True
        
        count = 0
        for passengerDetail in details:
            if not isCorrect(passengerDetail):
                raise Exception()
            
            if int(passengerDetail[11:13]) > 60:
                count += 1
        return count
            

            

