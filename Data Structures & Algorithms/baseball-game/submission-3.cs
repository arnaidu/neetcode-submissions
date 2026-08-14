public class Solution {
    public int CalPoints(string[] operations) {
        var stack = new List<int>();
        foreach (var op in operations) {
            if (op == "+") {
                stack.Add(stack[^1] + stack[^2]);
            } else if (op == "D") {
                stack.Add(2 * stack[^1]);
            } else if (op == "C") {
                stack.RemoveAt(stack.Count - 1);
            } else {
                int.TryParse(op, out var opInt);
                stack.Add(opInt);
            }
        }

        return stack.Sum();
    }
}