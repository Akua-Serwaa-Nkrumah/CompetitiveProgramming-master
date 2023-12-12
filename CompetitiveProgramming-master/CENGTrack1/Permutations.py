class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def is_valid_state(state):
            return len(state) == len(nums)

        def get_candidates(state):
            if len(state) == 0:
                return nums

            res = [num for num in nums if num not in state]
            return res

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state,solutions)
                state.remove(candidate)

            return

        def solve():
            state = []
            solutions = []
            search(state, solutions)
            return solutions

        return solve()

    
    