# - - - - - - Roman Numeral to Integer - - - - - - #
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num_val = 0

        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                num_val += roman_num_dict[s[i+1]] - roman_num_dict[s[i]]
                i += 2  # Skip the next character as it's already processed
            else:
                num_val += roman_num_dict[s[i]]
                i += 1
        
        return num_val
