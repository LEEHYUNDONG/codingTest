#include < iostream>
#include <vector>
using namespace std;

class Solution
{
    int maxArea(vector<int> & height)
    {
        int l = 0;
        int r = height.size() - 1;

        int a = INT_MIN;
        while (l < r)
        {
            int len = r - l;
            int h = min(height[l], height[r]);
            a = max(a, len * h);
            if (height[l] > height[r])
                r--;
            else
                l++;
        }
        return a;
    }
}
int main()
{

    return 0;
}