#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    vector<int> n;
    for (int i = 0; i < 5; i++)
    {
        n.push_back(i);
    }
    do
    {
        for (auto a : n)
        {
            cout << a << " ";
        }
        cout << "\n";
    } while (next_permutation(n.begin(), n.end()));
}