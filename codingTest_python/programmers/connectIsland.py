def solution(n, costs):

    # 부모 찾아주기
    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return parent[x]

    # 합치기 연산
    def union_find(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = 0
    parent = [0]*n
    # 부모 테이블 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i

    costs.sort(key=lambda x: x[2])

    for edge in costs:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_find(parent, a, b)
            answer += cost

    return answer
