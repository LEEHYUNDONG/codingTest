#include <string>
#include <vector>

using namespace std;

int solution(string s)
{
    int answer = 0;
    string ans = "";
    string tmp = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] >= '0' && s[i] <= '9')
        {
            ans += s[i];
        }
        else if (s[i] <= 'z' && s[i] >= 'a')
        {
            tmp += s[i];
        }
        if (tmp == "zero")
        {
            ans += '0';
            tmp = "";
        }
        else if (tmp == "one")
        {
            ans += '1';
            tmp = "";
        }
        else if (tmp == "two")
        {
            ans += '2';
            tmp = "";
        }
        else if (tmp == "three")
        {
            ans += '3';
            tmp = "";
        }
        else if (tmp == "four")
        {
            ans += '4';
            tmp = "";
        }
        else if (tmp == "five")
        {
            ans += '5';
            tmp = "";
        }
        else if (tmp == "six")
        {
            ans += '6';
            tmp = "";
        }
        else if (tmp == "seven")
        {
            ans += '7';
            tmp = "";
        }
        else if (tmp == "eight")
        {
            ans += '8';
            tmp = "";
        }
        else if (tmp == "nine")
        {
            ans += '9';
            tmp = "";
        }
    }
    return stoll(ans);
}