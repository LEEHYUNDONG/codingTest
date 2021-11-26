#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> m;
    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        if (num == 0 && !m.empty())
        {
            m.pop_back();
        }
        else
        {
            m.push_back(num);
        }
    }
    if (m.empty())
    {
        cout << 0 << '\n';
    }
    else
        cout << accumulate(m.begin(), m.end(), 0) << '\n';

    return 0;
}