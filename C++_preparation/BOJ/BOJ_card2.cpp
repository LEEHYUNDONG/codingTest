#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> q;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        q.push(i);
    }
    int i = 0;
    while (q.size() != 1)
    {
        if (i % 2 == 0)
            q.pop();
        else
        {
            int tmp = q.front();
            q.pop();
            q.push(tmp);
        }
        i++;
    }
    cout << q.front() << '\n';

    return 0;
}