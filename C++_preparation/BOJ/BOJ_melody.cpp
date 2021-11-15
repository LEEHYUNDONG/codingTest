#include <iostream>
#include <string>

using namespace std;

int main()
{
    string data;
    char tmp;
    for (int i = 0; i < 8; i++)
    {
        cin >> tmp;
        data += tmp;
    }

    if (data == "12345678")
        cout << "ascending\n";
    else if (data == "87654321")
        cout << "descending\n";
    else
        cout << "mixed\n";
    return 0;
}