# Coin Change

## Problem

Find minimum coins to make amount.


## Idea

DP

dp[x] = min coins for x


## Algorithm

1. dp[0] = 0
2. try every coin
3. update dp
4. return dp[amount]


## Complexity

Time: O(n * amount)

Space: O(amount)


## Code

See solution.py