#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{

    string s = "ABEFDES";

    do
    {
        for (char a : s)
        {
            cout << a << " ";
        }
        cout << endl;

    } while (next_permutation(s.begin(), s.end()));
    return 0;
}