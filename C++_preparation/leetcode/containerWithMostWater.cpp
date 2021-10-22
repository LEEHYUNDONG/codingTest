#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int ans = 0;
        int h = 10000;
        for (int i = 0; i < height.size(); i++)
        {
            // int width = -1;
            int h1 = height[i];
            for (int j = height.size() - 1; j > i; j--)
            {
                int width = j - i;
                int h2 = height[j];
                h = min(h1, h2);
                ans = max(ans, width * h);
                cout << h << " " << width << " " << height[i] << " " << height[j] << '\n';
            }
        }

        return ans;
    }
};

int main()
{
    Solution s;
    vector<int> tmp;
    tmp.push_back(2);
    tmp.push_back(3);
    tmp.push_back(4);
    tmp.push_back(5);
    tmp.push_back(18);
    tmp.push_back(17);
    tmp.push_back(6);
    cout << s.maxArea(tmp) << '\n';

    return 0;
}