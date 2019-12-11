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
