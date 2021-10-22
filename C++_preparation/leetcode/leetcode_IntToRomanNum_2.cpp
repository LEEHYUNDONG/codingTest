#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        vector<int> n = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> s = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans = "";
        int i = 0;
        while (num)
        {
            int r = num / n[i];
            while (r--)
            {
                ans += s[i];
            }
            num = num % n[i];
            i++;
        }
        return ans;
    }
};
int main()
{
    Solution t;
    cout << t.intToRoman(3504) << endl;
    return 0;
}