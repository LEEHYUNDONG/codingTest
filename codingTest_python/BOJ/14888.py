import sys
input = sys.stdin.readline

def dfs(nums, plu, minus, mul, div, tot):
    global ans
    if plu == 0 and minus == 0 and mul == 0 and div == 0:
        ans = max(ans, tot)
    