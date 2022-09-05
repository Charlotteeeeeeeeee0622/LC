class UndergroundSystem:

    def __init__(self):
        self.idstation={}
        self.pairs=Counter()
        self.freq=Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idstation[id]=stationName,t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevn,prevt=self.idstation.pop(id)
        self.pairs[prevn,stationName]+=t-prevt
        self.freq[prevn,stationName]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pairs[startStation,endStation]/self.freq[startStation,endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)