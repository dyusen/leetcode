class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        prev = 0

        for roman_num in s[::-1]:
            value = roman_symbols[roman_num]
            if value >= prev:
                res += value
            else:
                res -= value
            prev = value

        return res


r = Solution()
print(r.romanToInt("MCDXLIV"), 1444)
print(r.romanToInt("III"), 3)
print(r.romanToInt("IV"), 4)
print(r.romanToInt("MCMXCIV"), 1994)
