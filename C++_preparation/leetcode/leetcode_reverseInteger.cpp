#include <string>
#include <iostream>
using namespace std;
int solution(int x)
{
    int k = abs(x - 0);
    long long ans = 0;
    while (k > 0)
    {
        int rem = k % 10;
        k = k / 10;
        ans = ans * 10 + rem;
    }
    if (x < 0)
    {
        ans *= -1;
    }
    if (ans < INT_MIN || ans > INT_MAX)
        return 0;
    else
        return (int)ans;
}
int main()
{
    cout << solution(100231231) << '\n';
    return 0;
}