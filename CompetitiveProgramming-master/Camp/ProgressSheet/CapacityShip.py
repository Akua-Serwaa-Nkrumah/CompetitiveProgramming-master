class Solution:
    def shipWithinDays(self, weights: [int], days: int) -> int:
        
        def check(mid):
            count = 0
            day = 1
            for weight in weights: 
                if count + weight > mid:
                    day += 1
                    count = 0 

                count += weight
                
            return day

        l, r = max(weights), sum(weights)

        while l <= r:
            mid = l + (r-l)//2

            if check(mid) <= days:
                r = mid - 1
            else: 
                l = mid + 1
        
        return l

        

        