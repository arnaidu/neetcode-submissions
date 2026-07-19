public class MinStack {

    private readonly Stack<int> _stack;
    private readonly Stack<int> _min;
    public MinStack() {
        _stack = new Stack<int>();
        _min = new Stack<int>();
    }
    
    public void Push(int val) {
        _stack.Push(val);

        if (_min.Count > 0)
        {
            // minimum up to this point;
            _min.Push(Math.Min(_min.Peek(), val));
        }
        else
        {
            _min.Push(val);
        }
    }
    
    public void Pop() {
        _stack.Pop();
        _min.Pop();
    }
    
    public int Top() {
        return _stack.Peek();
    }
    
    public int GetMin() {
        return _min.Peek();
    }
}
