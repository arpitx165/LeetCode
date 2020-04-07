"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prof =0
        i=1
        while(i < len(prices)):
            if(prices[i] < prices[i-1]):
                i+=1
            else:
                val = prices[i-1]
                while(i<len(prices) and prices[i] >= prices[i-1]):
                    i+=1
                prof+=(prices[i-1]-val)   
        return prof