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
    int map[501][501];
    memset(map, 0, sizeof(map));
    int height[w];
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
        for (int j = 0; j < x; j++)
        {
            map[i][j] = 1;
        }
        height[i] = x;
    }
    int rh = 0;
    int ans = 0;

    for (int i = 0; i < maxh; i++)
    {
        int tmp = 0;
        for (int j = 0; j < h; j++)
        {
            if (map[i][j] == 1)
            {
                tmp += 1;
            }
        }
        for (int j = 0; j < rh; j++)
        {
            if (map[i][j] == 0)
            {
                map[i][j] = 2;
            }
        }
        if (rh < tmp)
        {
            rh = tmp;
        }
        else if (rh >= tmp)
        {
            ans += (rh - tmp);
        }
    }
    rh = height[w - 1];
    for (int i = w - 1; i > maxh; i--)
    {
        int tmp = 0;
        for (int j = 0; j < h; j++)
        {
            if (map[i][j] == 1)
            {
                tmp += 1;
            }
        }
        for (int j = 0; j < rh; j++)
        {
            if (map[i][j] == 0)
            {
                map[i][j] = 2;
            }
        }
        if (rh < tmp)
        {
            rh = tmp;
        }
        else if (rh >= tmp)
        {
            ans += (rh - tmp);
        }
    }
    // for (int i = 0; i < w; i++)
    // {
    //     for (int j = 0; j < h; j++)
    //     {
    //         cout << map[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    cout << ans << endl;
    return 0;
}