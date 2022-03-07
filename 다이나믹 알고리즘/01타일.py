n = int(input())
dp = [0]*(n+2)
dp[0] = 1 # 1
dp[1] = 2 # 00 11
for i in range(n):
    if i >= 2:
        dp[i] += (dp[i-1]+dp[i-2])%15746
print(dp[n-1])




