Ссылка: https://leetcode.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        while n!=1 and n!=4:
            s = 0
            while n>0:
                d = n%10
                s+=d*d
                n//=10
            n = s
        return n==1
