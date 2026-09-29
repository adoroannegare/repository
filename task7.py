Ссылка: https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        stek = []
        sl = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stek.append(char)
            else:
                if len(stek)==0:
                    return False
                else:
                    if stek[-1] != sl[char]:
                        return False
                    stek.pop()
        return len(stek)==0
                
