class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
            return false;
        string sx = to_string(x);
        int start = 0;
        int end = sx.length() - 1;
        if (x % 2)
        { // 홀수 일 때
            int mid = (start + end) / 2;
            while (start <= mid or end >= mid)
            {
                if (sx[start] != sx[end])
                    return false;
                start++;
                end--;
            }
            return true;
        }
        else
        { //짝수 일때.
            while (start < end)
            {
                if (sx[start] != sx[end])
                    return false;
                start++;
                end--;
            }
            return true;
        }
    }
};