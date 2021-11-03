#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(vector<int> numbers, string hand)
{
    string answer = "";
    vector<pair<int, int> > dial = {{4, 2}, {1, 1}, {1, 2}, {1, 3}, {2, 1}, {2, 2}, {2, 3}, {3, 1}, {3, 2}, {3, 3}};

    int lx = 4, ly = 1;
    int rx = 4, ry = 3;
    for (int i = 0; i < numbers.size(); i++)
    {
        int tx = dial[numbers[i]].first, ty = dial[numbers[i]].second;
        int rd = abs(rx - tx) + abs(ry - ty);
        int ld = abs(lx - tx) + abs(ly - ty);

        if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9)
        {
            rx = tx;
            ry = ty;
            answer += 'R';
        }
        else if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7)
        {
            lx = tx;
            ly = ty;
            answer += 'L';
        }
        else
        {
            if (rd < ld)
            {
                answer += 'R';
                rx = tx;
                ry = ty;
            }
            else if (rd > ld)
            {
                answer += 'L';
                lx = tx;
                ly = ty;
            }
            else if (rd == ld)
            {
                if (hand == "right")
                {
                    answer += 'R';
                    rx = tx;
                    ry = ty;
                }
                else if (hand == "left")
                {
                    answer += 'L';
                    lx = tx;
                    ly = ty;
                }
            }
        }
    }
    return answer;
}