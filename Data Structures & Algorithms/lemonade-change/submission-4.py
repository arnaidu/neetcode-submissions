class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = 0
        BASE_COST = 5
        fives, tens = 0, 0

        for bill in bills:        
            need_to_payback = bill - BASE_COST
            if change < need_to_payback:
                return False
            
            if bill == 5:
                fives += 1            
            elif bill == 10:
                if fives < 1:
                    return False
                tens += 1
                fives -= 1
                change += 5
            else:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                
            change += 5

        
        return True
