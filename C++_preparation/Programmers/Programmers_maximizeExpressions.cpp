#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <deque>
typedef long long ll;

using namespace std;

ll solution(string expression)
{
    ll answer = 0;
    vector<ll> res;
    string op = "";
    deque<ll> num;

    int idx = 0;
    for (int i = 0; i < expression.length(); i++)
    {
        if (expression[i] >= '0' && expression[i] <= '9')
        {
            continue;
        }
        else if (expression[i] == '-' || expression[i] == '*' || expression[i] == '+')
        {
            num.push_back(stoi(expression.substr(idx, i - idx)));
            // if(expression[i] == '-') {
            //     op += '+';
            //     idx = i;
            //     continue;
            // }
            op += expression[i];
            idx = i + 1;
        }
    }
    num.push_back(stoi(expression.substr(idx, expression.length() - idx)));

    // for(auto a : num){
    //     cout << a << endl;
    // }
    // cout << op << endl;
    for (int i = 0; i < op.length(); i++)
    {
        ll a = num[i], b = num[i + 1];
        num.pop_front();
        num.pop_front();
        if (op[i] == '*')
        {
            num.push_front(a * b);
            op.erase(i, i + 1);
        }
        else if (op[i] == '+')
        {
            num.push_front(a + b);
            op.erase(i, i + 1);
        }
    }
    answer = abs(num.front());
    return answer;
}