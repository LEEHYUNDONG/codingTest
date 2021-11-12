#include <iostream>

using namespace std;

int n, r, c;
int ans;

void z(int i, int j, int size)
{
    if (i == r && j == c)
    {
        cout << ans << '\n';
        return;
    }
    if (r >= i && r < i + size && c >= j && c < j + size)
    {
        z(i, j, size / 2);
        z(i, j + size / 2, size / 2);
        z(i + size / 2, j, size / 2);
        z(i + size / 2, j + size / 2, size / 2);
    }
    else
    {
        ans += size * size;
    }
}
int main()
{
    cin >> n >> r >> c;
    z(0, 0, (1 << n));
    return 0;
}