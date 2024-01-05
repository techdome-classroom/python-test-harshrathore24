class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        pre_value = 0

        for char in s:
            value = translations[char]
            if value > pre_value:
                number += value - 2 * pre_value
            else:
                number += value

            pre_value = value

        return number
