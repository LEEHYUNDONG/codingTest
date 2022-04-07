#include <bits/stdc++.h>
using namespace std;

int answer = 0;
vector<pair<int, int> > moves;

void hanoi(int n, int from, int via, int to)
{
    if (n == 1)
    {
        moves.push_back(make_pair(from, to));
        return;
    }
    hanoi(n - 1, from, to, via);
    moves.push_back(make_pair(from, to));
    hanoi(n - 1, via, from, to);
}
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    hanoi(n, 1, 2, 3);

    cout << moves.size() << '\n';
    for (auto a : moves)
    {
        cout << a.first << " " << a.second << '\n';
    }

    return 0;
}