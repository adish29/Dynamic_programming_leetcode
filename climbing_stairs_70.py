class Solution:
    def climbStairs(self, n: int) -> int:
        S = []
        S = [0] * (n + 1)
        if n == 1:
            return 1
        # if number of steps are 0 then there are 0
        # different ways.
        S[0] = 0
        # if one step then only single way
        S[1] = 1
        # if two steps then two ways,
        # first way: 1 + 1
        # second way: 2
        S[2] = 2
        if n == 2:
            return S[2]
        for i in range(3, n+1):
            # there are two different ways to reach the kth step
            # Step 1. take 1 step from (k-1)th step
            # Step 2. take 2 steps from (k-2)th step
            S[i] = S[i-1] + S[i-2]
        # Distinct ways to climb n steps can be found at S[n]
        return S[n]