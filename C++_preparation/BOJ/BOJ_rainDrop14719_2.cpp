#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;

int main()
{
    int h, w; //세로 가로 길이
    // ios_base::sync_with_stdio;
    cin.tie(0);
    cout.tie(0);
    cin >> h >> w;
    int maxh = 0;
    int height[501];
    int he = 0;
    for (int i = 0; i < w; i++)
    {
        int x;
        cin >> x;
        if (x > he)
        {
            he = x;
            maxh = i;
        }

        height[i] = x;
    }
    int rh = 0;
    int ans = 0;

    for (int i = 0; i < maxh; i++)
    {

        if (rh < height[i])
        {
            rh = height[i];
        }
        else if (rh >= height[i])
        {
            ans += (rh - height[i]);
        }
    }
    rh = height[w - 1];
    for (int i = w - 1; i > maxh; i--)
    {

        if (rh < height[i])
        {
            rh = height[i];
        }
        else if (rh >= height[i])
        {
            ans += (rh - height[i]);
        }
    }

    cout << ans << endl;
    return 0;
}