#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(int n)
{
    string answer = "";
    vector<string> s = {"1", "2", "4"};

    while (n > 0)
    {
        int c = n % 3;
        if (c == 0)
        {
            answer += s[2];
            n -= 1;
        }
        else if (c == 1)
            answer += s[0];
        else if (c == 2)
            answer += s[1];
        // cout << n << endl;
        n /= 3;
    }
    reverse(answer.begin(), answer.end());
    return answer;
}