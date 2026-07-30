public class LRUCache {

    private int _size;
    private Dictionary<int, Node> _cache;
    private Node _lruStart;
    private Node _lruEnd;

    public LRUCache(int capacity) {
        _size = capacity;
        _cache = new();
    }
    
    public int Get(int key) {
        if (!_cache.TryGetValue(key, out var node)) {
            return -1;
        }

        MoveToStart(node);
        return node.Value;
    }

    public void MoveToStart(Node node) {
        if (_lruStart == node) return;

        if (node.Prev != null) node.Prev.Next = node.Next;
        if (node.Next != null) node.Next.Prev = node.Prev;
        if (_lruEnd == node && node.Prev != null) _lruEnd = node.Prev;

        node.Prev = null;
        node.Next = _lruStart;
        if (_lruStart != null) _lruStart.Prev = node;
        _lruStart = node;
        if (_lruEnd == null) _lruEnd = node;
    }

    public void RemoveEnd() {
        if (_lruEnd == null) return;
        _cache.Remove(_lruEnd.Key);
        if (_lruStart == _lruEnd) {
            _lruStart = _lruEnd = null;
        } else {
            _lruEnd = _lruEnd.Prev;
            _lruEnd.Next = null;
        }
    }
    
    public void Put(int key, int value) {
        if (!_cache.TryGetValue(key, out var node)) {
            if (_cache.Count == _size) {
                RemoveEnd();
            }

            node = new Node {
                Key = key,
                Value = value,
            };

            _cache.Add(key, node);
            MoveToStart(node);
            return;
        }

        node.Value = value;
        MoveToStart(node);
    }
}

public class Node {
    public int Key { get; set; }
    public int Value { get; set; }
    public Node Next { get; set; }
    public Node Prev { get; set; }
}
