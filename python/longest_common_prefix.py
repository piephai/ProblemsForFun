
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final_string: str = ""
        length_shortest_str = len(sorted(strs, key=len)[0])
        if length_shortest_str == 0:
            return final_string
        print(length_shortest_str)
        for i in range(length_shortest_str + 1):
            temp = [str[:i] for str in strs]
            print(f"Iteration of {i} with values {temp}")
            if temp.count(temp[0]) == len(temp):
                final_string = temp[0]
                if (i == length_shortest_str):
                    return final_string

            else:
                if len(final_string) > 0:
                    return final_string
                else:
                    return ""

    # Optimised solution frm Leetcode
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     arr=sorted(strs,key=len)
    #     result=""
    #     for i in range(len(arr[0])):
    #         for j in range(1,len(arr)):
    #             if arr[0][i]!=arr[j][i]:
    #                 return result
    #         result+=arr[0][i]
    #     return result                

sol = Solution()
#roman_strings = [["flower", "flow", "flight"],["dog", "daddy", "dj"] ]
#roman_strings = [["a"]]
roman_strings = [["ab", "a"]]
#roman_strings = [["flower","flower","flower","flower"]]
#roman_strings = [["", "", ""]]
roman_string: str
for roman_string in roman_strings:
    ans = sol.longestCommonPrefix(roman_string)
    print(f"Answer is {ans}")
