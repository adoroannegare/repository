
 #Ссылка:https://leetcode.com/problems/longest-common-prefix/
    def longestCommonPrefix(self, strs):
        first = strs[0]
        if not strs:
            return ""
        for i, char in enumerate(first):
            for s in strs[1::]:
                if i >= len(s) or s[i] != char:
                    return first[:i]
        return first
