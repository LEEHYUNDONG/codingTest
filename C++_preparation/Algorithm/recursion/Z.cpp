#include <bits/stdc++.h>
using namespace std;
int ans = 0;
int r = 0, c = 0;
bool found = false;

void searchZ(int x, int y, int size)
{
    if (x == r && y == c)
    {
        cout << ans;
        return;
    }
    // r, c 목표하는게 해당 범위에 들어오면 recursive하게 찾는다.
    if (x <= r && r < x + size && y <= c && c < y + size)
    {
        int rz = size / 2;
        searchZ(x, y, rz);           //제 1사분면
        searchZ(x, y + rz, rz);      //제 2사분면
        searchZ(x + rz, y, rz);      //제 3사분면
        searchZ(x + rz, y + rz, rz); //제 4사분면
    }
    else //범위 내에 존재하지 않는다면 size만큼 그냥 더하기
    {
        ans += size * size;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N >> r >> c;

    searchZ(0, 0, (1 << N));

    return 0;
}