public class Solution {
    public bool LemonadeChange(int[] bills) {
        var collectedBills = new Dictionary<int, int>();
        foreach (var bill in bills) {
            var change = bill - 5;
            while (collectedBills.GetValueOrDefault(10) > 0 && change >= 10) {
                change -= 10;
                collectedBills[10] -= 1;
            }

            while (collectedBills.GetValueOrDefault(5) > 0 && change >= 5) {
                change -= 5;
                collectedBills[5] -= 1;
            }

            if (change > 0) {
                return false;
            }

            collectedBills[bill] = collectedBills.GetValueOrDefault(bill) + 1;
        }

        return true;
    }
}