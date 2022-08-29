class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.pos={}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            # 把新加的放最后
            self.pos[val]=len(self.nums)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            ind=self.pos[val]
            last=self.nums[-1]
            self.nums[ind]=last
            self.pos[last]=ind
            self.nums.pop()
            self.pos.pop(val,0)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()