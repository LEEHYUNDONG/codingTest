#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    string room;
    vector<int> num(10, 0);
    cin >> room;
    for (int i = 0; i < room.size(); i++)
    {
        if (room[i] == '6' || room[i] == '9')
        {
            if (num[6] < num[9])
            {
                num[6]++;
                continue;
            }
            else if (num[6] > num[9])
            {
                num[9]++;
                continue;
            }
        }
        num[(int)room[i] - '0']++;
    }
    cout << *max_element(num.begin(), num.end()) << '\n';

    return 0;
}