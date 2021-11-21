#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    int arr[100001] = {0};
    int tot;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    int s, e;

    for (int i = 1; i < n; i++)
        arr[i] += arr[i - 1];
    for (int i = 0; i < m; i++)
    {
        cin >> s >> e;
        if (s == 1)
        {
            cout << arr[e - 1] << '\n';
            continue;
        }
        cout << arr[e - 1] - arr[s - 2] << '\n';
    }

    return 0;
}