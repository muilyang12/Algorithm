MODULO = 1000000007


def countBalancedClips(clipLength, diff):
    dp = [[0, [0 for _ in range(26)]] for __ in range(clipLength + 1)]
    dp[1][0] = 26
    dp[1][1] = [1 for _ in range(26)]

    for i in range(2, clipLength + 1):
        currentSum = 0

        for j in range(26):
            for k in range(-diff, diff + 1):
                if j + k < 0 or j + k >= 26:
                    continue

                dp[i][1][j] += dp[i - 1][1][j + k]

            dp[i][1][j] %= MODULO

            currentSum += dp[i][1][j]

        dp[i][0] = currentSum % MODULO

    return dp[-1][0]
