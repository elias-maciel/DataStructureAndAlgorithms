from typing import Dict


class Solution:
    symbol_map: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def roman_algarisms_to_int(self, s: str) -> int:
        m = {}
        m['I'] = 1
        m['V'] = 5
        m['X'] = 10
        m['L'] = 50
        m['C'] = 100
        m['D'] = 500
        m['M'] = 1000
        num = m[s[len(s) - 1]]
        pre = num
        for i in range(len(s) - 2, -1, -1):
            cur = m[s[i]]
            if cur < pre:
                num -= cur
            else:
                num += cur
            pre = cur

        return num
