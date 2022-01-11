## Binary Search
> 이진 탐색은 배일이 정렬되어 있어야 사용할 수 있는 알고리즘

데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 장점이 있다.

### 코딩 테스트에서의 이진 탐색
> 이진 탐색은 구현 문제와 함께 사용될 수 있는 확률이 높음. 그러므로 코드를 되도록 외워두는 것이 유리하다. 아니면 bisect를 이용해도 됨.

### 빠르게 입력 받기
이진 탐색 문제는 입력 데이터가 많거나, 탐색 범무이가 매우 넓은 편이다. 예를 들어 데이터의 개수가 1,000만 갤르 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심해야한다. 그런데 이렇게 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려져서 시간 초과로 오답 판정을 받을 수 있다. 