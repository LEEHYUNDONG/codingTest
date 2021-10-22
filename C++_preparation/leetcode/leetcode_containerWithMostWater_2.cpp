#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int maxCont = INT_MIN;

        int l = 0;
        int r = height.size() - 1;

        while (l < r)
        {

            int len = r - l;
            maxCont = max(maxCont, len * min(height[l], height[r]));

            if (height[l] > height[r])
                r--;
            else
                l++;
        }

        return maxCont;
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