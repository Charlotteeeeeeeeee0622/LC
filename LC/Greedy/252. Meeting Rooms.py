class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        e = 0
        for start, end in intervals:
            if start >= e:
                e = end
            else:
                return False

        return True

#     def canAttendMeetings(self, intervals):
#         intervals.sort(key=lambda x: x.start)

#         for i in range(1, len(intervals)):
#             if intervals[i].start < intervals[i-1].end:
#                 return False

#         return True
