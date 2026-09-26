Ссылка: https://leetcode.com/problems/length-of-last-word/submissions/2154250090/
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
