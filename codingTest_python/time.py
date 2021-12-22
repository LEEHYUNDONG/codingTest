# h = int(input())

# cnt = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):  # 문자열로 바꾸어 생각하는게 키포인트
#                 cnt += 1
# print(cnt)


# 시각
N = int(input())
cnt = 0
# N시 59분 59초 까지
for i in range(N+1):
    if (i == 3) or (i % 10 == 3):
        cnt += 60 * 60
        continue
    for j in range(60):
        if (j % 10 == 3) or (j // 10 == 3):
            cnt += 60
            continue
        for k in range(60):
            if (k % 10 == 3) or (k // 10 == 3):
                cnt += 1
                continue

print(cnt)
