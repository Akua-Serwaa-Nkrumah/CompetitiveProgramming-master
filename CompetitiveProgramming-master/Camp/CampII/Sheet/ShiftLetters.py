class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        def num(letter):
            return ord(letter) - ord('a') + 1

        dif = [0]*(len(s)+2)
    
        for shift in shifts:
            l,r,k = shift[0], shift[1], shift[2]
            if k == 0:
                dif[l+1] -= 1
                dif[r+2] += 1
            else:
                dif[l+1] += 1
                dif[r+2] -= 1

        res = ''

        for i in range(1,len(s)+1):
            dif[i] += dif[i-1]

        for i in range(1,len(s)+1):
            dif[i] += num(s[i-1])

        print(dif)
        for i in range(1,len(s)+1):
            if dif[i]%26 == 0:
                res += 'z'
            else:
                res += chr(dif[i]%26 +96)

        return res