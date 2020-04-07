"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = {}
        while(True):
            if(n in mem):
                return False
            else:
                mem[n]=1
            if n == 1:
                return True
            tmp = n
            n=0
            while(tmp):
                n+= (tmp%10)*(tmp%10)
                tmp/=10