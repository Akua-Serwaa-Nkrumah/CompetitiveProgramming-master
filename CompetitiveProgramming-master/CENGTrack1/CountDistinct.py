class Solution(object):
    def countDistinctIntegers(self, nums):
        new_nums = []
        for i in nums:
            num_str = str(i)
            num_rev = num_str[::-1]
            str_num = int(num_rev)
            new_nums.append(str_num)
        new_nums.extend(nums)
        new_nums = set(new_nums)

        return len(new_nums)
akua = Solution()
print(akua.countDistinctIntegers([1,13,10,12,31]))