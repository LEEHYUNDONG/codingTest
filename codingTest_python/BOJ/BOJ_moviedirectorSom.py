import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
six = 666

while True:
    if '666' in str(six):
        # 매 숫자의 크길르 1씩 증가시킬 때 마다 숫자에 연속된 3개의 6이 존재하면 cnt개수를 올리고 즉 cnt는 n과 비교되어 가장 작은 n번째 숫자가 될 수 밖에 없다.
        cnt += 1
    if cnt == n:
        print(six)
        break
    # 부르트포스 알고리즘으로 숫자를 단순히 증가시켜서 그 숫자내에 666, 즉 6이 연속적으로 존재하는 경우를 찾는 것임.
    six += 1
