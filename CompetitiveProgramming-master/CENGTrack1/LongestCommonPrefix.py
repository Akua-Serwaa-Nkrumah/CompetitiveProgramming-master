class Solution(object):
    def longestCommonPrefix(self, strs):
      strs = sorted(strs)
      common = ""
      for i in range(len(strs[-1])):
         if len(strs[0])>i and strs[-1][i] == strs[0][i]:
               common += strs[-1][i]
         else:
               return common
      return common


