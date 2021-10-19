#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> vec;
    for (int i = 1; i <= 10; i++)
    {
        vec.push_back(i * 10);
    }
    for (vector<int>::iterator iter = vec.begin(); iter != vec.end(); ++iter)
    {
        cout << *iter << endl;
    }
    return 0;
}