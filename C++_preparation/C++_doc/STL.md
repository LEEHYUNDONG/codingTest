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

```c++
vector<int> v; //비어있는 벡터 생성
vector<int> v(5);
vector<int> v(5, 2);

v.assign(5, 2); // 2의 값으로 5개 원소 할당.
v.front();
v.back();
v.clear();
v.push_back(7);
v.pop_back();
```
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
## 👉 deque의 함수들
#### 👉 Iterator
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
---
## 🌳 algorithm
c++ 표준 라이브러리의 <algorithm> 라이브러리에는 원소들에 대해 작업할 수 있는 여러가지 함수(검색, 정렬, 원소 수정, 개수 세기 등등)들을 정의하고 있다. 이 때 작업할 원소들은 반복자 혹은 포인터를 통해 가리킬 수 있으며, 아래 함수들의 경우 작업을 시작할 원소와 작업을 끝낼 원소 바로 뒤를 인자로 받게 된다.

### 🌳 원소를 수정하지 않는 작업들
- all_of :범위 안에 모든 원소들이 조건을 만족하는지 확인
- any_of :범위 안에 원소들 중 조건을 만족하는 원소가 있는지 확인.

## 🌳 문자열 관련 함수 및 STL

### 🙈 stringstream 사용법
문자열을 나누는 stringstream c++에서 주어진 문자열에서 필요한 자료형에 맞는 정볼르 꺼낼 때 융요하게 사용된다. stringstream에서 공백과 '\n'을 제외하고 문자열에서 맞는 자료형의 정보를 빼낸다.

`#include <sstream> 전처리 헤더를 포함 시킨다.`
stream.str(string str)현재 stream의 값을 문자열 str로 변환시킨다.

```c++
int num;
string str = "123 456";
stringstream stream;
stream.str(str);
while(stream1 >> num){
	cout << num << '\n';
}
```

### 🙈 to_string 함수
```c++
string to_string(int num);
string to_string(long num);
string to_string(long long num);
string to_string(unsigned num);
string to_string(unsigned long num);
string to_string(float num);
string to_string(double num);
string to_string(long double num);
/*
함수 설명
숫자 타입의 데이터를 안전하게 스트링 타입으로 변경하도록하는 함수입니다.
*/
```
### 🙈 std::stoi, std::stol, std::stoll

```c++
// stoi 함수
int stoi(const std::string& str, std::size_t* pos = 0, int base = 10);
int stoi(const std::wstring& str, std::size_t* pos = 0, int base = 10);
// stol 함수
long stol(const std::string& str, std::size_t* pos = 0, int base = 10);
long stol(const std::wstring& str, std::size_t* pos = 0, int base = 10);
// stoll 함수
long long stoll(const std::string& str, std::size_t* pos = 0, int base = 10);
long long stoll(const std::wstring& str, std::size_t* pos = 0, int base = 10);
```
string 또는 wstring 문자열 str을 base 진법을 사용하는 부호 있는 정수로 변환한 값을 리턴한다. 이때, 변환 과정에서 문자를 읽었는지는 Pos에 저장된다.
이때 문자열을 정수로 해석할 때 다음의 과정에 따라 해석을 한다. 먼저 맨 앞에 붙어 있는 공백 문자들 (isspace() 호출 시 true인 애들)을 공백 문자가 아닌 문자가 나올 때 까지 무시한다. 그 뒤 base 진법이라 써진 것에 따라서 문자를 읽어들인다.

#### ✌️ 인자
- str :반환할 문자열
- pos :문자열에서 문자 몇 개를 읽어들였는지 저장할 위치
- base :정수 변환 시에 사용할 진법
#### ✌️ 예외
- 변환이 불가능 할 때, `std::invalid_argument`
- 변환한 값이 정수 범위를 초과한다면 `std::out_of_range`
---
## 🌳 숫자관련 STL

### c/c++ pow 함수 원형과 사용법
`#include <cmath>를 포함시킨다.`

#### ✌️ 함수 원형
```c++
double pow(double base, double n);
float pow(float base, float n);
long double pow(long double base, long double n);

```