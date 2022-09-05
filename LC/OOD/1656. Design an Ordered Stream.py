class OrderedStream:

    def __init__(self, n: int):
        self.data=[None]*n
        self.prt=0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.data[idKey]=value
        if idKey>self.prt:return []
        while self.prt < len(self.data) and self.data[self.prt]:
            self.prt += 1 # update self.ptr
        return self.data[idKey:self.prt]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)