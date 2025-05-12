class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        lowest_point = 0
        maximum_point = 0
        for i in range(len(intervals)):
            lowest_point = min(intervals[i][0], lowest_point)
            maximum_point = max(intervals[i][1], maximum_point)
		return