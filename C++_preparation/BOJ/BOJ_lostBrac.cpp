#include <iostream>
#include <string>
#include <vector>

using namespace std;

int ans;

int main()
{
    string exp;
    cin >> exp;

    string tn = "";
    int tot = 0;
    bool flag = false;

    for (int i = 0; i <= exp.size(); i++)
    {
        if (exp[i] == '+' || exp[i] == '-' || i == exp.size())
        {
            if (flag)
                tot -= stoi(tn);

            else
                tot += stoi(tn);
            tn = "";
        }
        else
        {
            tn += exp[i];
        }
        if (exp[i] == '-')
            flag = true;
    }

    cout << tot << '\n';
    return 0;
}