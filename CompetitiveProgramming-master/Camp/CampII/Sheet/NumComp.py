class Solution:
    def findComplement(self, num: int) -> int:
        binary = ''

        while num != 0:
            binary += str((num-1)%2)
            num >>= 1
        
        binary = binary[::-1]
        
        return int(binary,2)