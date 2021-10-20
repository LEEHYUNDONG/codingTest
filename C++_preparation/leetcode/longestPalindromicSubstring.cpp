#include <string.h>
#include <iostream>
using namespace std;

class Solutions
{
public:
    string longestPalindrome(string s)
    {
        // code here
        int low, high;
        int start = 0, end = 1;
        for (int i = 1; i < s.length(); i++)
        {
            //홀수일 때
            low = i - 1;
            high = i;
            while (low >= 0 and high < s.length() and s[low] == s[high])
            {
                if (high - low + 1 > end)
                {
                    start = low;
                    end = high - low + 1;
                }
                low--;
                high++;
            }
            // 짝수의 경우일 때
            low = i - 1;
            high = i + 1;
            while (low >= 0 and high < s.length() and s[low] == s[high])
            {
                if (high - low + 1 > end)
                {
                    start = low;
                    end = high - low + 1;
                }
                low--;
                high++;
            }
        }
        string str = "";
        end = start + end - 1;
        for (int i = start; i <= end; i++)
        {
            str += s[i];
        }
        return str;
    }
};