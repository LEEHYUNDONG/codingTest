#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> vec;
    for (int i = 0; i <= 10; i++)
        vec.push_back(i * 10);

    for (int i = 0; i <= 10; i++)
    {
        cout << vec[i] << '\n';
    }
    return 0;
}