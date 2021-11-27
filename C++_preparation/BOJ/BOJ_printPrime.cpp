#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int pn[1000001] = {0};
    int n, m;
    cin >> m >> n;
    for (int i = 2; i <= n; i++)
        pn[i] = i;

    for (int i = 2; i <= sqrt(n); i++)
    {
        if (pn[i] == 0)
            continue;
        for (int j = i + i; j <= n; j += i)
        {
            pn[j] = 0;
        }
    }
    for (int i = m; i <= n; i++)
    {
        if (pn[i] != 0)
            cout << i << '\n';
    }
    return 0;
}