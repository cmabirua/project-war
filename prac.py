class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        all_num=0
        prev_num=0
        for i in s:
            num=roman[i]
            if num>=prev_num:
                num-=prev_num
                all_num+=num
                prev_num=num
        return all_num       #roman to int