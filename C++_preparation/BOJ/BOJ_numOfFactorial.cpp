#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int tmp = n / 5;
    int tmp2 = n / 25;
    int tmp3 = n / 125;
    cout << tmp + tmp2 + tmp3 << endl;

    return 0;
}