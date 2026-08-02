public class Solution {
    public string SimplifyPath(string path) {
        string[] splitPath = path.Split("/");
        Stack<string> stack = [];

        foreach (var pathElement in splitPath) {
            if (pathElement == "" || pathElement == ".") {
                // skip '/' for now and '.' is same dir so can skip
                continue;
            }

            if (stack.Count > 0 && pathElement == "..") {
                if (stack.Peek() == "/") {
                    continue;
                }

                stack.Pop(); // move up one directory
                continue;
            }

            if (pathElement != "..") {
                stack.Push(pathElement);
            }
        }

        return "/" + string.Join('/', stack.Reverse());
    }
}