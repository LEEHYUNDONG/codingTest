import sys
input = sys.stdin.readline

def dfs(nums, plu, minus, mul, div, tot, idx):
    global ans_max
    global ans_min
    if idx == N:
        ans_max = max(ans_max, tot)
        ans_min = min(ans_min, tot)
    if plu > 0:
        dfs(nums, plu-1, minus, mul, div, tot + nums[idx], idx+1)
    if minus > 0:
        dfs(nums, plu, minus-1, mul, div, tot - nums[idx], idx+1)
    if mul > 0:
        dfs(nums, plu, minus, mul-1, div, tot * nums[idx], idx+1)
    if div > 0:
        dfs(nums, plu, minus, mul, div-1, int(tot / nums[idx]), idx+1)
    

N = int(input())
nums = list(map(int, input().split()))
pl, ms, ml, dv = map(int, input().split())
ans_max, ans_min = -int(1e9), int(1e9)

dfs(nums, pl, ms, ml, dv, nums[0], 1)
print(ans_max)
print(ans_min)