# House Robber

## Problem

Cannot rob adjacent houses.
Find max money.


## Idea

DP

dp[i] = max(
  dp[i-1],
  dp[i-2] + nums[i]
)


## Algorithm

1. iterate
2. choose rob or skip
3. keep best


## Complexity

Time: O(n)

Space: O(1)


## Code

See solution.py