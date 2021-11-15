#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int data[5];
    for (int i = 0; i < 5; i++)
    {
        cin >> data[i];
    }
    int tot = 0;
    for (auto a : data)
        tot += pow(a, 2);
    cout << tot % 10 << endl;
}
