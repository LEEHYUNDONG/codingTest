#include <iostream>

using namespace std;
int fib(int n)
{
    if (n <= 0)
        return 1;
    cout << n << endl;
    return fib(n - 1) * n;
}
int main()
{

    cout << fib(10)<< endl;
    return 0;
}