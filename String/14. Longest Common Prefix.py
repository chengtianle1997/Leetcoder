class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = min([len(string) for string in strs])
        
        i = 0
        res = ""
        while i < min_len:
            target = strs[0][i]
            for string in strs:
                if not target == string[i]:
                    return res
            res += target
            i += 1
        return res