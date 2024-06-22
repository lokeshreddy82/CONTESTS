class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        requirements.sort()
        MOD = 10**9 + 7
        # Initialize the DP table
        dp = [[0] * 401 for _ in range(n + 1)]
        dp[0][0] = 1

        # Initialize the next DP table to apply requirements
        next_dp = [[0] * 401 for _ in range(n + 1)]

        for length in range(1, n + 1):
            for inv in range(401):
                dp[length][inv] = 0
                for k in range(length):
                    if inv - k >= 0:
                        dp[length][inv] = (dp[length][inv] + dp[length - 1][inv - k]) % MOD

            # Apply requirements after filling dp for current length
            for endi, cnti in requirements:
                if endi == length - 1:
                    for inv in range(401):
                        next_dp[length][inv] = 0
                    if cnti < 401:
                        next_dp[length][cnti] = dp[length][cnti]
                    dp[length] = next_dp[length][:]

        # Result is the number of valid permutations for the entire array
        return dp[n][requirements[-1][1]]
