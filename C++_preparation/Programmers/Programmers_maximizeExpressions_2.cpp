#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

typedef long long ll;

using namespace std;

ll solution(string expression)
{
    ll answer = 0;
    vector<ll> res;
    vector<char> oper = {'+', '-', '*'};
    sort(oper.begin(), oper.end());
    vector<char> op;
    vector<ll> num;

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
            op.push_back(expression[i]);
            idx = i + 1;
        }
    }
    num.push_back(stoi(expression.substr(idx, expression.length() - idx)));

    do
    {
        vector<ll> tmp_num = num;
        vector<char> tmp_op = op;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < tmp_op.size(); j++)
            {
                ll tmp = 0;
                ll a = tmp_num[j], b = tmp_num[j + 1];
                if (tmp_op[j] == oper[i])
                {
                    if (tmp_op[j] == '+')
                        tmp_num[j] = a + b;
                    else if (tmp_op[j] == '-')
                        tmp_num[j] = a - b;
                    else if (tmp_op[j] == '*')
                        tmp_num[j] = a * b;
                    tmp_num.erase(tmp_num.begin() + j + 1); //한 개만 지우고 나머지 하나는 대입함;;;아오
                    tmp_op.erase(tmp_op.begin() + j);
                    j--;
                }
            }
        }
        if (answer < abs(tmp_num.front()))
            answer = abs(tmp_num.front());

    } while (next_permutation(oper.begin(), oper.end()));

    return answer;
}