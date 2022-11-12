class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        
        for i in range(len(strs[0])):
            # print(i)
            for s in strs:
                if i == len(s) or s[i] != strs[0][i] :
                    return res 
                # print(s)
            res += strs[0][i]
        return res