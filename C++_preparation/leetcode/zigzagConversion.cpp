#include <iostream>
#include <stdio.h>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
    // string s = "PAYPALISHIRING";
    // int numrow = 3;
    // vector<vector<char> > vc;
    // int cnt = 0;
    // for (int i = 0; i < s.size(); i++)
    // {
    //     cout << s[cnt] << endl;
    //     if (cnt == numrow)
    //     {
    //         while (((numrow / 2) + numrow) != cnt)
    //         {
    //             cout << "s[cnt] :" << s[cnt] << ' ';
    //             cnt++;
    //         }
    //         cout << '\n';
    //         // i = cnt;
    //     }
    //     cnt++;
    // }
    vector<string> v;
    int numRows = 3;
    int r = numRows;
    string s = "PAYPALISHIRING";
    while (r != 0)
    {
        v.push_back("");
        r--;
    }
    int row = 0;
    int step = 1;
    if (r == 1)
    {
        step = 0;
    }
    stringstream ss;
    for (int i = 0; i < s.length(); i++)
    {
        v[row] += s[i];
        cout << row << step << endl;
        row += step;
        if (row + 1 == numRows || row == 0)
        {
            step = -step;
        }
    }
    for (int i = 0; i < v.size(); i++)
    {
        ss << v[i];
        cout << "v[" << i << "] :" << v[i] << '\n';
    }
    s = ss.str();
    for (int i = 0; i < s.size(); i++)
    {
        cout << s[i];
    }
    cout << '\n';
    return 0;
}