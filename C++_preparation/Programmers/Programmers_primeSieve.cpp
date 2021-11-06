#include <string>
#include <vector>
#include <memory.h>

int a[1000001];

using namespace std;

int solution(int n)
{
    int answer = 0;
    memset(a, 0, sizeof(a));

    for (int i = 2; i < n + 1; i++)
    {
        a[i] = i;
    }

    for (int i = 2; i * i <= n; i++)
    {
        if (a[i] == 0)
            continue;
        for (int j = i + i; j <= n; j += i)
        {
            a[j] = 0;
        }
    }

    for (int i = 2; i < n + 1; i++)
    {
        if (a[i] != 0)
            answer++;
    }

    return answer;
}