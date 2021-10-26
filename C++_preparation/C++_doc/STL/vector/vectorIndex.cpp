#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> vec = {1, 22, 3, 4, 5, 6, 23};
    int index = find(vec.begin(), vec.end(), 4) - vec.begin();
    cout << "The loc of 4 :" << index << endl;
    return 0;
}