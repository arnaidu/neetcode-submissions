public class MyQueue {
    public Stack<int> _stack = new();
    public Stack<int> _reverseStack = new();

    public MyQueue() {
        
    }
    
    public void Push(int x) {
        _stack.Push(x);
    }
    
    public int Pop() {
        if (_reverseStack.Count > 0) {
            return _reverseStack.Pop();
        }

        Arrange();

        return _reverseStack.Pop();
    }
    
    public int Peek() {
        if (_reverseStack.Count > 0) {
            return PeekInternal();
        }

        Arrange();

        return PeekInternal();
    }

    private int PeekInternal() {
        var value = _reverseStack.Pop();
        _reverseStack.Push(value);
        return value;
    }
    
    public bool Empty() {
        return (_stack.Count + _reverseStack.Count) == 0;
    }

    private void Arrange() {
        if (_reverseStack.Count > 0) {
            return;
        }

        while (_stack.Count > 0) {
            _reverseStack.Push(_stack.Pop());
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */