#include <stdio.h>
#include <vector>

int main()
{
    unordered_map<char, int> window;
    int left = 0, right = 0;

    int res = 0;
    while (right < s.size())
    {
        char c = s[right];
        right++;
        window[c]++;

        if (window[c] <= 1)
            res = max(right - left, res);
        while (window[c] > 1)
        {
            char d = s[left];
            left++;
            window[d]--;
        }
    }
    cout << res << '\n';
    return 0;
}