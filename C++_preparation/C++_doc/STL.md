# 👤 C++ STL 컨테이너 정리
## 🌳 Vector
- C++ STl 컨테이너 두 가지 종류
	
	- 시퀀스 컨테이너
		- 배열처럼 객체들을 순차적으로 보관
		- 시퀀스 컨테이너의 경우 `vector, list, deque` 이렇게 세 가지가 정의되어 있다.
	- 연관 컨테이너 
		- 키를 바탕으로 대응되는 값을 찾아주는 것이다.
- vector
	- 가변길이 배열
	- 벡터에는 원소들이 메모리 상에서 실제로 순차적으로 저장되어 있고, 따라서 임의의 위치에 있는 원소를 접근하는 것을 매우 빠르게 수행할 수 있다.

- vector의 임의의 원소에 접근하는 것은 배열처럼 	`[]` or `at`함수를 이용한다.
- 벡터의 크기를 리턴하는 함수인 size의 경우 리턴하는 값의 타입은 size_type 멤버 타입으로 정의되어 있다.
- 맨 뒤에 원소를 추가하거나 제거하기 위해서는 push_back 혹은 pop_back 함수를 사용하면된다. 

## 🌳 deque
`deque는 queue와 비슷하지만 queue는 front에서만 삭제가 가능하고, end에 삽입하는데 deque는 양방향으로 삽입, 삭제가 모두 가능하다.`
- 연속적인 메모리를 기반으로 하는 순차 컨테이너
- 벡터와 함수가 거의 비슷하지만, push_front(), pop_front()가 가능하고, capacity()는 안된다.
- 임의의 원소에 접근이 가능하다. 인덱스가 존재.
- resize를 통해 크기 변경이 가능하고, 크기가 가변적이기 때문에 삽입할 때 크기 고려하지 않아도 된다.
```c++
#include <deque>

deque<int> dq1; //비어있는 deque 생성
deque<int> dq(4); //0으로 초기화 된 4 개의 원소를 가진 deque를 생성한다.
deque<int> dq = {1, 2, 3};
deque<int> dq{1, 2, 3};
```
### deque의 함수들
#### Iterator
dq.begin(), dq.end()
```c++
dq.assign(5) //원소 5개 0으로 초기화
dq.assign(5, 10) //원소 5개 10으로 초기화
dq.front()
dq.back()
dq.at()

dq.push_front(n)
dq.oush_back(n)
dq.pop_front()
dq.pop_back()
dq.insert(v.begin(), n)
dq.size()
dq.resize(10)
dq.clear()
dq.erase(v.begin()) //iterator가 가리키는 원소 삭제
```