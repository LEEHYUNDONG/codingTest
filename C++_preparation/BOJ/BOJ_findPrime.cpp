#include <iostream>

using namespace std;
bool isPrime(int x)
{
    if (x == 1 || x == 0)
        return false;
    for (int i = 2; i < x; i++)
    {
        if (x % i == 0)
            return false;
    }
    return true;
}
int main()
{
    int n;
    cin >> n;
    int pr[101];
    int cnt = 0;

    for (int i = 0; i < n; i++)
        cin >> pr[i];
    for (int i = 0; i < n; i++)
    {
        if (isPrime(pr[i]))
            cnt++;
    }
    cout << cnt << '\n';

    return 0;
}