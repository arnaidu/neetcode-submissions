public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        Stack<int> tempIdxs = new();
        int[] result = new int[temperatures.Length];
        for (int today = 0; today < temperatures.Length; today++) {
            while (tempIdxs.Count > 0 && temperatures[tempIdxs.Peek()] < temperatures[today]) {
                int pastDay = tempIdxs.Pop();
                int numDaysPassed = today - pastDay;
                result[pastDay] = numDaysPassed;
            }

            tempIdxs.Push(today);
        }

        return result;
    }
}
