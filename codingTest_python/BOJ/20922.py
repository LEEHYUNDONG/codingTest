'''
N인 수열이 주어진다.  이 수열에서 같은 정수를 
K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.
조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.
9 2
3 2 5 5 6 4 4 5 7
2 4 4 5 7 -> 5

7
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

def check(dic, N, K):
    for key in dic.keys():
        if dic[key] > K:
            return False
    return True

N, K = map(int, input().split())
arr = list(map(int, input().split()))
numDic = defaultdict(int)
l, r = 0, 0

while r < N and l <= r:
    # K개가 안넘는지 확인
    numDic[arr[r]] += 1
    r += 1

print(numDic)
print(r - l + 1)