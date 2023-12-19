class Solution:
    def numRescueBoats(self, people: [int], limit: int) -> int:
        people = sorted(people)
        num = 0
        l, r = 0, len(people) - 1

        while l <= r:
            
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1

            num += 1

        return num




        