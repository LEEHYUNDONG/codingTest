l = ['A', 'B', 'C', 'D']

for ii in enumerate(l):
    print(ii[0], ii[1])

'''
enumerate 함수는 인자의 값을 추출할 때 인덱스를 추출하는 기법이다. 함수를 사용하면
인덱스 번호와 컬렉션의 원소를 튜플 형태로 반환한다.
'''

n = [1, 2, 3, 4]
m = ['a', 'b', 'c', 'd']
for i in zip(n, m):
    print(i)

'''
zip은 여러 개의 순회 가능한 객체를 인자로 받아 동일한 개수로 이루어진 자료형을
묶어서 튜플의 형태로 반환한다.
'''