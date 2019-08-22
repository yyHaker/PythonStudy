#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.会议室II.py
@time: 2019/8/21 10:46
"""
"""
leetcode253,题目：Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), 
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
"""
思路：使用优先队列算法, 生成优先队列(最小堆), 代表已开的房间, 先将时间段按照开始时间排序, 
遍历时间段, 如当前会议室安排不下这个会议, 则将这个会议加到队列里（新开一个会议室）, 如果能找到房间且目
前会议的起始之间在上个会议的终止时间之后, 更新队列.
Time: O(n)
Space: O(1)
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        # sort the intervals by start time
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                # room is already used in last meeting and continue to use the same room for this meeting
                heapq.heapreplace(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)

        return len(heap)

# test
intervals = [[0, 30], [5, 10], [15, 20]]
inters = []
for interval in intervals:
    inter = Interval(interval[0], interval[1])
    inters.append(inter)
solution = Solution()
res = solution.minMeetingRooms(inters)
print(res)
