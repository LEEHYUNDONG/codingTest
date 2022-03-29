import sys
input = sys.stdin.readline

n = int(input())
blog = list(input().strip())

cnt = {'R' : 0, 'B' : 0}
cnt[blog[0]] += 1
for i in range(1, n):
    if blog[i] != blog[i-1]:
        cnt[blog[i]] += 1

print(min(cnt['R'], cnt['B'])+1)

# B 1
# R 1
# B 2
# R 2
# B 3
# R 3