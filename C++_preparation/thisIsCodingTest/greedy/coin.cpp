#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> coin = {500, 100, 50, 10};
    int cnt = 0;
    int money;
    cin >> money;
    for (int i = 0; i < coin.size(); i++)
    {
        cnt += money / coin[i];
        money %= coin[i];
    }
    cout << cnt << '\n';
    return 0;
}