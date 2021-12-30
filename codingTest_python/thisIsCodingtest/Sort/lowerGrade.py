n = int(input())

student = []

for _ in range(n):
    i = input().split()
    student.append([i[0], int(i[1])])

student = sorted(student, key=lambda x: x[1])
for i in student:
    print(i[0], end=' ')
print()
