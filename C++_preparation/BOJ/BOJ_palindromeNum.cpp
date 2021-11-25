#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    while (1)
    {
        string tmp = "";
        cin >> tmp;
        if (tmp == "0")
            break;
        else
        {
            string l, r;
            int mid = tmp.length() / 2;
            if (tmp.length() % 2)
            {
                l = tmp.substr(0, mid);
                r = tmp.substr(mid + 1, tmp.length());
            }
            else
            {
                l = tmp.substr(0, mid);
                r = tmp.substr(mid);
            }
            reverse(r.begin(), r.end());
            if (l == r)
                cout << "yes\n";
            else if (l != r)
                cout << "no\n";
        }
    }
    return 0;
}