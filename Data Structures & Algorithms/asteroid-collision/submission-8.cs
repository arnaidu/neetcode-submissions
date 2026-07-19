public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        Stack<int> asteroidStack = new();

        foreach (var ast in asteroids) {
            bool destroyed = false;

            while (asteroidStack.Count > 0 && asteroidStack.Peek() > 0 && ast < 0) {
                int top = asteroidStack.Peek();

                if (Math.Abs(top) < Math.Abs(ast)) {
                    asteroidStack.Pop();
                    continue;
                }
                else if (Math.Abs(top) == Math.Abs(ast)) {
                    asteroidStack.Pop();
                }

                destroyed = true;
                break;
            }

            if (!destroyed) {
                asteroidStack.Push(ast);
            }
        }

        return asteroidStack.Reverse().ToArray();
    }
}