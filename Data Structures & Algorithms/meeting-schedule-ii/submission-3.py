"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Minimum number of meeting rooms required = max number of overlapping meetings at any give time. We keep two arrays start and end with the start and end times of a meeting sorted. We keep incrementing start counter while start time <= end time. Keep track of a count var per iteration of end time. Update res to be max of count time during traversal.

0,5,15 10,20,40
'''
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        count = 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        i,j = 0,0 # i -> end, j -> start

        while j < len(end):
            if start[j] < end[i]:
                count += 1
                j += 1
            else:
                i += 1
                count -= 1
            res = max(res,count)

        return res

        