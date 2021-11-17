#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int num, bit = 0;
    string op;

    while (n--)
    {

        cin >> op;
        if (op == "add")
        {
            cin >> num;
            bit |= (1 << num);
        }
        else if (op == "remove")
        {
            cin >> num;
            bit &= ~(1 << num);
        }
        else if (op == "check")
        {
            cin >> num;
            if (bit & (1 << num))
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
        else if (op == "toggle")
        {
            cin >> num;

            bit ^= (1 << num);
        }
        else if (op == "all")
        {
            bit = (1 << 21) - 1;
        }
        else if (op == "empty")
        {
            bit = 0;
        }
    }
    return 0;
}