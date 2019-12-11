def maximum_profit_unlimited_dp(prices):
    # given an array of prices:
    # what is the max. profit you can make by buying and selling
    # as often as you want?
    n = len(prices)
    if n == 0:
        return 0
    s, t = [None] * n, [None] * n
    s[0], t[0] = -prices[0], 0
    for i in range(1, n):
        t[i] = max(prices[i] + s[i-1], t[i-1])
        s[i] = max(-prices[i] + t[i-1], s[i-1])
    return t[n-1]


def maximum_profit_limited_dp(prices, k):
    # given an array of prices:
    # what is the max. profit you can make by buying and selling
    # at most k times (buying k times and selling k times)
    n = len(prices)
    if n == 0:
        return 0
    s = [[0 for _ in range(n)] for _ in range(k+1)]
    t = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(k+1):
        s[i][0], t[i][0] = -prices[0], 0
    for j in range(1, k+1):
        for i in range(1, n):
            t[j][i] = max(prices[i] + s[j][i-1], t[j][i-1])
            s[j][i] = max(-prices[i] + t[j-1][i-1], s[j][i-1])
    return t[k][n-1]
