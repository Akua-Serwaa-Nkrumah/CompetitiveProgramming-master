class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        change = {5:0,10:0,20:0}

        for i in bills:
            if i == 10:
                if change[5] > 0:
                    change[5] -= 1
                else:
                    return False

                change[10] += 1

            elif i == 5:
                change[5] += 1

            else:
                if change[10] > 0:
                    change[10] -= 1
                    if change[5] > 0:
                        change[5] -= 1

                    else:
                        return False
                elif change[5] < 3:
                    return False
                else:
                    change[5] -= 3

                change[20] += 1

        return True