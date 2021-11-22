#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int arr[1000001];
    int n, m;
    cin >> n >> m;
    cin >> arr[0];
    for (int i = 1; i < n; i++)
    {
        cin >> arr[i];
        arr[i] += arr[i - 1];
    }
    for (int i = 0; i < m; i++)
    {
        int s, e;
        cin >> s >> e;
        if (s == 1)
            cout << arr[e - 1] << '\n';
        else
            cout << arr[e - 1] - arr[s - 2] << '\n';
    }

    return 0;
}