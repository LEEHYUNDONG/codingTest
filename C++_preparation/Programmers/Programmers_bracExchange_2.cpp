#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool check(string p)
{
    int cnt = 0;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == '(')
            cnt++;
        else
            cnt--;
        if (cnt < 0)
            return false;
    }

    return (cnt == 0);
}

string solution(string p)
{
    if (p == "")
        return p;
    int l, r = 0;
    string u, v;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == '(')
            l++;
        if (p[i] == ')')
            r++;
        if (l == r)
        {
            u = p.substr(0, i + 1);
            v = p.substr(i + 1);
            break;
        }
    }
    if (check(u))
        return u + solution(v);

    string answer = "(" + solution(v) + ")";

    for (int i = 1; i < u.size() - 1; i++)
    {
        answer += (u[i] == '(' ? ")" : "(");
    }
    return answer;
}