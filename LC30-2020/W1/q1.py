"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=0
        for i in nums:
            val^=i
        return val