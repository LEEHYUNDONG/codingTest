# append는 자료형 그대로 붙여준다.
arr = [1, 2, 3, 4]
arr.append([1, 2])
print(arr)

# extend는 list안에 원소들을 빼서 원래 자료형을 확장시켜준다.
arr = [1, 2, 3, 4]
arr.extend([1, 2])
print(arr)
