"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ans = 0
        min_num = -1e18
        max_cur=0
        for i in nums:
            max_cur+=i
            max_ans = max(max_ans, max_cur)
            if max_cur < 0:
                max_cur=0
            min_num = max(min_num,i)
        if max_ans == 0:
            return min(max_ans, min_num)
        return max_ans