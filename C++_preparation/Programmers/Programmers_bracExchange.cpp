#include <string>
#include <queue>
using namespace std;

bool check(string p)
{
    queue<char> b;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == '(')
        {
            b.push(p[i]);
        }
        else if (p[i] == ')')
        {
            if (!b.empty() && b.front() == '(')
                b.pop();
            else
                return false;
        }
    }
    return true;
}
string solution(string p)
{
    if (p == "")
        return p;

    int cnt = 0;
    string u, v;

    for (int i = 0; i < p.size(); i++)
    {
        if (p[i] == '(')
            cnt++;
        else
            cnt--;
        if (cnt == 0)
        {
            u = p.substr(0, i + 1);
            v = p.substr(i + 1);
            break;
        }
    }

    if (check(u))
        return u + solution(v);

    string ret = "(" + solution(v) + ")";
    for (int i = 1; i < u.size() - 1; i++)
        ret += (u[i] == '(' ? ")" : "(");

    return ret;
}