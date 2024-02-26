s = input()

dp = [0]*(len(s) + 1)
dp[0] = 1
def solve():
    for i in range(1,len(s)):
        if s[i] == 'm' or s[i] == 'w':
            return 0
        
        dp[i] = dp[i-1]

        if (s[i] == 'n' or s[i] == 'u') and s[i] == s[i-1]:
            dp[i] += dp[i
                        -2]
            dp[i]%= (1000000007)

    return dp[len(s)]

print(solve())