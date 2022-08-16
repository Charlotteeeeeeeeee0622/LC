# https://leetcode.com/problems/meeting-rooms-ii/discuss/67917/Python-heap-solution-with-comments.
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)