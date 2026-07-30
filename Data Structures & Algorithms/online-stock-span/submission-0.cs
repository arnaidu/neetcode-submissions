public class StockSpanner {

    private Stack<(int price, int span)> _prices;
    public StockSpanner() {
        _prices = [];
    }
    
    public int Next(int price) {
        int span = 1;
        while (_prices.Count > 0 && _prices.Peek().price <= price) {
            (int prevPrice, int prevSpan) = _prices.Pop();
            span += prevSpan;
        }

        _prices.Push((price, span));
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */