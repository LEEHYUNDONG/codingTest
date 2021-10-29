#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;
int getN(int N, int idx)
{
    // NN(idx = 1), NNN(idx==2), NNNN(idx==3) N을 사용해서 만들수 있는 숫자 인덱스 반환해주는 함수
    int res = N;

    for (int i = 1; i <= idx; i++)
    {
        res = res * 10 + N; // 10씩 증가시켜서 그 숫자 값을 만들어준다.
    }
    return res;
}
int solution(int N, int number)
{
    if (N == number)
        return 1;
    vector<unordered_set<int> > dp(8);
    dp[0].insert(N);
    for (int k = 1; k < 8; k++)
    {
        dp[k].insert(getN(N, k));
        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                if (i + j + 1 != k)
                    continue;
                for (int a : dp[i])
                {
                    for (int b : dp[j])
                    {
                        dp[k].insert(a + b);

                        if (a - b > 0)
                            dp[k].insert(a - b);
                        dp[k].insert(a * b);
                        if (a / b > 0)
                            dp[k].insert(a / b);
                    }
                }
            }
        }
        if (dp[k].find(number) != dp[k].end())
            return k + 1;
    }
    for (int i = 0; i < 8; i++)
    {
        cout << i << "*" << endl;
        for (auto a : dp[i])
        {
            cout << a << endl;
        }
    }
    return -1;
}
int main()
{
    solution(5, 12);
    cout << solution(5, 12) << '\n';
    return 0;
}