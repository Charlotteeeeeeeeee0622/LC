class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        e=-float('inf')
        count=0
        intervals.sort(key=lambda i:i[-1])
        for start,end in intervals:
            if start>=e:
                e=end
            else:
                count+=1
        return count