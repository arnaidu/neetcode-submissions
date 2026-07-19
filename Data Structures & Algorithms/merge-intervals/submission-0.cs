public class Solution {
    private readonly int _start = 0;
    private readonly int _end = 1;
    public int[][] Merge(int[][] intervals) {
        // sort by start times
        Array.Sort(intervals, (a, b) => a[_start].CompareTo(b[_start]));

        List<int[]> output = new();
        int[] prevInterval = intervals[0];
        output.Add(intervals[0]);
        for (int i = 1; i < intervals.Length; i++) {
            var currInterval = intervals[i];
            if (currInterval[_start] <= prevInterval[_end])
            {
                prevInterval[_end] = Math.Max(prevInterval[_end], currInterval[_end]);
            }
            else
            {
                output.Add(currInterval);
                prevInterval = currInterval;
            }
        }

        return output.ToArray();
    }
}
