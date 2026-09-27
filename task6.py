Ссылка: https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        s = int(''.join(str(s) for s in digits))
        return [int(x) for x in str(s+1)]
