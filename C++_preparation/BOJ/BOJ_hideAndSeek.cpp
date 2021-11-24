#include <iostream>
#include <queue>

using namespace std;
bool check[100001] = {false};
int main()
{
    queue<int> q;
    int n, m;
    int loc, cnt = 0;
    int res[100001] = {0};

    cin >> n >> m;

    q.push(n);
    check[n] = true;

    while (!q.empty())
    {
        loc = q.front();
        q.pop();
        if (loc == m)
            break;
        if (0 <= loc - 1 && !check[loc - 1])
        {
            check[loc - 1] = true;
            res[loc - 1] = res[loc] + 1;
            q.push(loc - 1);
        }
        if (loc + 1 <= 100001 && !check[loc + 1])
        {
            check[loc + 1] = true;
            res[loc + 1] = res[loc] + 1;
            q.push(loc + 1);
        }
        if (2 * loc <= 100001 && !check[2 * loc])
        {
            check[loc * 2] = true;
            res[loc * 2] = res[loc] + 1;
            q.push(2 * loc);
        }
    }

    cout << res[m] << endl;
    return 0;
}