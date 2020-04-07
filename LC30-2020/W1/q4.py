"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        st = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                while(st < i  and nums[st]!=0):
                    st+=1
                if st < i and st !=i:
                    tmp = nums[i]
                    nums[i] = nums[st]
                    nums[st] = tmp
        return nums