#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int arr[1001];
    int cnt = 0;

    for (int i = 0; i <= n; i++)
        arr[i] = i;

    for (int i = 2; i <= n; i++)
    {
        for (int j = i; j <= n; j += i)
        {
            if (arr[j] == 0)
                continue;
            arr[j] = 0;
            cnt++;
            if (cnt == k)
            {
                cout << j << '\n';
                break;
            }
        }
    }

    return 0;
}