#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int cnt = 0;
    while (n >= k)
    {
        while (n % k != 0)
        {
            n--;
            cnt++;
        }
        n /= k;
        cnt++;
    }
    cout << cnt << '\n';
}