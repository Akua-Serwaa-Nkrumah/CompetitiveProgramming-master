class Solution(object):
    def smallestEvenMultiple(self, n):
        if(1<=n <=150):
            if (n%2 == 0):
                return n
            else:
                return n*2
        else:
            print("N must be between 1 and 150")