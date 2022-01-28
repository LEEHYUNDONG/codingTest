def solution(line):
    answer = []
    vertex = []
    for i in range(len(line)):
        a, b, c = line[i]
        for j in range(len(line)):
            d, e, f = line[j]
            if a*e == b*d or i == j:
                continue
            if (b*f-e*c) % (a*e-b*d) == 0 and (a*f-d*c) % (a*e-b*d) == 0:
                vertex.append(((b*f-e*c)//(a*e-b*d), (d*c-a*f)//(a*e-b*d)))

    vertex = list(set(vertex))
    maxV, minV = max(vertex)[0], min(vertex)[0]
    xx = [i[0] for i in vertex]
    yy = [i[1] for i in vertex]
    maxX, minX = max(xx), min(xx)
    maxY, minY = max(yy), min(yy)
    answer = [["."]*(maxX-minX+1) for _ in range(maxY-minY+1)]

    if len(vertex) == 1:
        return ['*']
    else:
        for x, y in vertex:
            answer[y-minY][x-minX] = '*'
        for i in range(len(answer)):
            answer[i] = ''.join(answer[i])
        return answer[::-1]
