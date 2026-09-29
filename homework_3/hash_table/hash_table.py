"""Задача 3. HashTable"""


class ChainingHashTable:
    """bucket = hash % m. Растем x2 при загрузке выше 1, не сжимаемся"""

    def __init__(self):
        self._buckets = [[] for _ in range(8)]
        self._size = 0

    def _bucket(self, key):
        return self._buckets[hash(key) % len(self._buckets)]

    def __getitem__(self, key):
        for pair in self._bucket(key):
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def __setitem__(self, key, value):
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self._size += 1
        if self._size > len(self._buckets):
            old = self._buckets
            self._buckets = [[] for _ in range(2 * len(old))]
            for bucket in old:
                for pair in bucket:
                    self._bucket(pair[0]).append(pair)

    def __delitem__(self, key):
        bucket = self._bucket(key)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def __len__(self):
        return self._size
