class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.maxcap = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {}

    def movetotail(self, key):
        cur = self.hashmap[key]

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        cur.prev = self.tail.prev
        cur.next = self.tail

        self.tail.prev.next = cur
        self.tail.prev = cur

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.movetotail(key)
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.movetotail(key)
            self.hashmap[key].value = value
        else:
            if len(self.hashmap) == self.maxcap:
                self.hashmap.pop(self.head.next.key)

                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            cur = Node(key, value)
            self.hashmap[key] = cur
            cur.prev = self.tail.prev
            cur.next = self.tail

            self.tail.prev.next = cur
            self.tail.prev = cur

            cur = Node(key, value)
            self.hashmap[key] = cur
            cur.prev = self.tail.prev
            cur.next = self.tail

            self.tail.prev.next = cur
            self.tail.prev = cur

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)