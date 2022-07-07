class Solution:
    def roman_to_int(self, s: str) -> int:       
        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total += roman_dict[s[i+1]] - roman_dict[s[i]]
                i += 2
            else:
                total += roman_dict[s[i]]
                i += 1
        return total


sol = Solution()
roman_strings = ["III", "LVIII", "MCMXCIV"]
roman_string: str
for roman_string in roman_strings:
    ans = sol.roman_to_int(roman_string)
    print(f"Answer is {ans}")
