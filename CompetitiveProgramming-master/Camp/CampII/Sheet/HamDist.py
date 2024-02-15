class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def binary(n):
            bn = ''

            while n != 0:
                bn += str(n%2)
                n >>= 1

            return bn

        bn_x = binary(x)
        bn_y = binary(y)
        mx = max(len(bn_x),len(bn_y))
        bn_x += '0'*(mx-len(bn_x))
        bn_y += '0'*(mx-len(bn_y))

        cnt = 0

        for i in range(min(len(bn_x),len(bn_y))):
            if bn_x[i] != bn_y[i]:
                cnt += 1

        print(bn_x,bn_y)

        return cnt
        