/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Interval> intervals) {
        if (intervals.Count == 0) {
            return true;
        }

        intervals.Sort((a, b) => a.start.CompareTo(b.start));
        var (prevStart, prevEnd) = (intervals[0].start, intervals[0].end);
        for (int i = 1; i < intervals.Count; i++) {
            var (currStart, currEnd) = (intervals[i].start, intervals[i].end);
            if (currStart < prevEnd) {
                return false;
            }

            prevStart = currStart;
            prevEnd = currEnd;
        }

        return true;
    }
}
