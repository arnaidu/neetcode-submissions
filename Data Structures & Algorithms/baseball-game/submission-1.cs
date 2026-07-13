public class Solution {
    public int CalPoints(string[] operations) {
        var scores = new Stack<int>();
        foreach (var op in operations) {
            if (op == "+") {
                var a = scores.Pop();
                var b = scores.Pop();
                var c = a + b;
                scores.Push(b);
                scores.Push(a);
                scores.Push(c);                
            }
            else if (op == "D") {
                var a = scores.Pop();
                scores.Push(a);
                scores.Push(2*a);
            }
            else if (op == "C"){
                scores.Pop();
            }
            else {
                int.TryParse(op, out var score);
                scores.Push(score);
            }
        }

        return scores.Sum();
    }
}