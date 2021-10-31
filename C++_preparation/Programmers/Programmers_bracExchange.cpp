#include <string>
#include <vector>
#include <queue>
#include <deque>

using namespace std;

bool checkBracket(string p)
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
            if (b.empty())
                return false;
            if (!b.empty() && b.front() == '(')
            {
                b.pop();
            }
        }
    }
    return true;
}
string make(string s, string u, string v)
{
    if (s == "")
        return "";
    string u = "";
    string v = "";
    deque<char> b;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(')
        {
            if (b.empty())
            {
                u += s[i];
                b.push_back(s[i]);
            }
            else if (!b.empty())
        }
        else if (s[i] == ')')
            if (!b.empty() && b.front() == '(')
            {
                u += s[i];
                b.pop_front();
            }
            else
            {
                v += s[i];
            }
    }
}
string solution(string p)
{
    string answer = "";
    // 올바른  문자열 리턴
    if (checkBracket(p))
        return p;

    string u = p;
    string v = "";
    // deque<char> tmp;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == ')')
        {
            tmp.push_back(p[i]);
        }
    }
    return answer;
}