class Solution:
        
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            for i in range(n):
                dp[i][i] = True
            palindrome_start, palindrome_len = 0, 1

            for end in range(0, n):
                for start in range(end - 1, -1, -1):
                    # print('start: %s, end: %s' % (start, end))
                    if s[start] == s[end]:
                        if end - start == 1 or dp[start + 1][end - 1]:
                            dp[start][end] = True
                            palindrome_len = end - start + 1
                            if palindrome_len < palindrome_len:
                                palindrome_start = start
                                palindrome_len = palindrome_len
            return s[palindrome_start: palindrome_start + palindrome_len]
