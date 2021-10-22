#include <stdio.h>
#include <vector>
#include <iostream>
#include <deque>
using namespace std;

int visited[10] = {0};
vector<int> v[10];

void bfs(int start)
{
    deque<int> q;
    visited[start] = 1;
    q.push_front(start);
    while (!q.empty())
    {
        int p = q.front();
        q.pop_front();
        cout << p << " ";
        for (int i = 0; i < v[p].size(); i++)
        {
            int y = v[p][i];
            if (!visited[y])
            {
                q.push_back(y);
                visited[y] = 1;
            }
        }
    }
}
int main()
{
    int n;
    cout << "How many edges"
         << "\n";
    cin >> n;
    cout << "From where to " << endl;
    for (int i = 0; i < n; i++)
    {
        int t1, t2;
        cin >> t1 >> t2;
        v[t1].push_back(t2);
        v[t2].push_back(t1);
    }
    int s = 0;
    cout << "Start from :";
    cin >> s;
    bfs(s);
    cout << '\n';
    cout << "thank u" << endl;

    return 0;
}