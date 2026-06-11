class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amount_change = { 20 : 0, 10 : 0, 5 : 0}
        for bill in bills:
            payment = bill
            for change in amount_change:
                while amount_change[change] > 0 and bill - change >= 5:
                    amount_change[change] -= 1
                    bill -= change
            
            amount_change[payment] += 1
            net_payment = bill
            if net_payment != 5:
                return False
        
        return True
