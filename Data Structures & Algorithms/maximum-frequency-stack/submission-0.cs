public class FreqStack {

    private Dictionary<int, int> _frequencies = new();
    private Dictionary<int, List<int>> _frequency_stack = new();
    private int _max_frequency = 0;

    public FreqStack() {
    }
    
    public void Push(int val) {
        // increment frequency
        if (!_frequencies.ContainsKey(val)) {
             _frequencies[val] = 0;
        }

        _frequencies[val] += 1;

        // keep track of stack for given frequency
        if (!_frequency_stack.ContainsKey(_frequencies[val])) {
            _frequency_stack[_frequencies[val]] = [];
        }

        // append to stack given frequency
        _frequency_stack[_frequencies[val]].Add(val);

        _max_frequency = Math.Max(_max_frequency, _frequencies[val]);        
    }
    
    public int Pop() {
        // grab max frequency in frequency stack
        List<int> stack = _frequency_stack[_max_frequency];

        // get rightmost value
        int val = stack[stack.Count - 1];
        stack.RemoveAt(stack.Count - 1);

        // reduce frequency of value
        _frequencies[val]--;
        
        // now if we have exhausted the current stack (i.e. it is empty), reduce max_frequency
        if (stack.Count == 0){
            _max_frequency--;
        }

        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.Push(val);
 * int param_2 = obj.Pop();
 */