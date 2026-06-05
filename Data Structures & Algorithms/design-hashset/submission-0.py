class MyHashSet:

    def __init__(self):
        self._num_buckets = 100
        self.hash_set = [[]] * self._num_buckets

    def add(self, key: int) -> None:
        bucket_idx = self._get_bucket(key)
        if self.contains(key):
            return
        self.hash_set[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._get_bucket(key)
        if self.contains(key):
            self.hash_set[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._get_bucket(key)
        return key in self.hash_set[bucket_idx]
        
    def _get_bucket(self, key: int) -> int:
        return key % self._num_buckets
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)