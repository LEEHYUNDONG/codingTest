from collections import Counter

d = Counter('hello World')

# 최대값 출력
print(max(d.values()))

# 데이터 캐수가 많은 순서대로 정렬된 배열 리턴
print(d.most_common())
