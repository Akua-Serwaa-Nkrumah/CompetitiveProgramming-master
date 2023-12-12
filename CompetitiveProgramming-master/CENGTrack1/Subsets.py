class Solution:
    def subsets(self, nums: [int]) -> [int]:

        def is_valid_state(state):
            return state.issubset(set(nums)) 

        def get_candidates(state):
            if len(state) == 0:
                return nums

            else:
                res = [num for num in nums if num > max(state)]

            return res

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        def solve():
            solutions = []
            state = set()
            search(state, solutions)
            return solutions
        
        return solve()