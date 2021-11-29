#include <iostream>
#include <string>
#include <stdlib.h> //abs를 활용하기 위해서

using namespace std;

int INF = 1000007;
int broken[10];

int Min(int a, int b)
{
    return a < b ? a : b;
}

bool possible(int k)
{
    if (k == 0)
        return broken[0] ? false : true;
    while (k)
    {
        if (broken[k % 10] == 1)
        {
            return false;
        }
        k /= 10;
    }

    return true;
}

int find(int N)
{
    int hundred = abs(N - 100);
    int button_min = INF;
    int temp;
    for (int i = 0; i <= INF; i++)
    {
        if (possible(i))
        {
            //버튼을 누른 횟수
            temp = to_string(i).length();
            //+,-를 해야하는 횟수
            temp += abs(i - N);
            //만일 이번 계산이 최소였다면, 저장하자.
            button_min = Min(button_min, temp);
        }
    }

    //가장 횟수가 적은 방법을 반환.
    return Min(hundred, button_min);
}

int main(void)
{
    int N, M, temp;
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> temp;
        broken[temp] = 1;
    }
    cout << find(N) << endl;
    return 0;
}
