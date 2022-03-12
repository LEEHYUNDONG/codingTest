# def clockTrans(size):
#     if size % 2:
#         size = (size // 2) + 1
#     else:
#         size = size // 2
    
#     while size:

#         size -= 1


# def counterclock():

def solution(n, clockwise):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    row, col = n-1, n-1 #행렬의 크기

    num = 1
    size = n-1
    x, y = 0, 0
    start = 0
    for i in range(start, size):
        y = i
        arr[x][y] = num
        num += 1
    size -= 1
    start += 1
    for i in range(start, size):
        x = i
        arr[x][y] = num
        num += 1
    size -= 1
    start += 1
    for i in range(start, size):
        y -= 1
        arr[x][y] = num
        num += 1
    size -= 1
    for i in range(start, size):
        x -= 1
        arr[x][y] = num
        num += 1
    for i in range(n):
        print(*arr[i])

        
    

    # return answer