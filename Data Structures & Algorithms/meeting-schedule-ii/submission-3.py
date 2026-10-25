"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        events = []

        for interval in intervals:

            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()

        count = 0
        maxSeen = 0

        for time, num in events:

            count+=num
            maxSeen = max(count, maxSeen)

        return maxSeen











        