public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        var bracketMap = new Dictionary<char, char>{
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };

        foreach (var ch in s){
            if (ch is ')' or ']' or '}' && stack.Count > 0) {
                // pop from stack and ensure we have equivalent opening bracket
                var openBracket = stack.Pop();
                if (bracketMap[ch] != openBracket) {
                    return false;
                }
            }
            else {
                stack.Push(ch);
            }
        }

        return stack.Count == 0;
    }
}
