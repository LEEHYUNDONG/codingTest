#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int arr[1001] = {0};
    int sum = 1;
    int cnt = 0;
    for (int i = 1; i <= k; i++)
    {
        arr[i] = sum;
        cnt++;
        if (cnt == sum)
        {
            sum++;
            cnt = 0;
        }
        arr[i] += arr[i - 1];
    }
    cout << arr[k] - arr[n - 1] << '\n';
    return 0;
}