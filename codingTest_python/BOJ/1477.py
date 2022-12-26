import sys
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))
hugeso = list(map(int, input().split()))

hugeso.sort()
print(*hugeso)
'''
모든 휴게소 사이사이에 값을 부르트포스로 삽입하고 최댓값을 계산하는 방식
'''