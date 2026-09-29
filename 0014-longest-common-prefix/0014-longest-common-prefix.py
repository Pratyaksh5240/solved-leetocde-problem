class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            ch = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]

        return strs[0]