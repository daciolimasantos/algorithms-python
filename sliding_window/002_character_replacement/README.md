# Longest Repeating Character Replacement

## Problem

Find longest substring with same letters
after at most k replacements.


## Idea

Sliding window.

Valid if:

window - max_freq <= k


## Algorithm

1. Expand right
2. Count chars
3. Shrink left if invalid
4. Track max


## Complexity

Time: O(n)

Space: O(1)


## Code

See solution.py