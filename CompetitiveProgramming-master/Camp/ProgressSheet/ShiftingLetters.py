class Solution:
    def shiftingLetters(self, s: str, shifts:[int]) -> str:

        shifts_sum = [shifts[-1]]*len(s)

        for i in range(len(s)-2,-1,-1):
            shifts_sum[i] = shifts[i] + shifts_sum[i+1]

        s = list(s)
        for j in range(len(shifts_sum)):
            num = shifts_sum[j] + ord(s[j])-97
            
            s[j] = chr(num%26 + 97)

        return ''.join(s)
        