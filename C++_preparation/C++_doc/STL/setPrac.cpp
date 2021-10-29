#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> s;

    for (int i = 1; i <= 5; i++)
    {
        s.insert(i * 10);
    }
    auto iter = s.find(30);
    if (iter != s.end())
        cout << "Yes we have 22" << '\n';
    else
        cout << "No we don't have" << '\n';
    for (auto i : s)
    {
        cout << i << endl;
    }
    return 0;
}