"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
"""
import hashlib
class Solution(object):
    
    def generateHash(self, s):
        return int(hashlib.sha1(s).hexdigest(), 16 % (10 ** 8))
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        val = {}
        for i in strs:
            mem = [0]*26
            for j in i:
                mem[ord(j)-97]+=1
            hash_val = ''
            for j in range(26):
                hash_val+= chr(97+j)+'_'+str(mem[j])+'_'
            hashed_val = self.generateHash(hash_val)
            if hashed_val in val:
                val[hashed_val].append(i)
            else:
                val[hashed_val] = [i]
        return [val[i] for i in val]