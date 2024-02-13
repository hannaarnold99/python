# - - - - - - Longest Common Prefix - - - - - - #
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefix = ''
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return prefix
            prefix += char

        return prefix
