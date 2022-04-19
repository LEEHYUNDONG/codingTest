H, W = map(int, input().split())
cont = list(map(int, input().split()))
stack = []
ans = 0


for i in range(W):
    if not stack:
        stack.append(cont[i])
    else:
        if stack[0] > cont[i]:
            stack.append(cont[i])
        else:
            tmp = min(stack[0], cont[i])
            while len(stack) >= 1:
                ans += (tmp - stack[-1])
                stack.pop()
            stack.append(cont[i])

tmp = min(stack[0], stack[-1])
stack.pop()
while len(stack) > 1:
    if tmp < stack[-1]:
        tmp = stack[-1]
    ans += (tmp-stack[-1])
    stack.pop()
print(ans)