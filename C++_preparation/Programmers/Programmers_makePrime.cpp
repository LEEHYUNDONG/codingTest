#include <vector>
#include <iostream>
using namespace std;

int ans = 0;
bool visited[1001] = {false};
vector<int> a;

bool isPrime(int n)
{
    int cnt = 0;
    for (int i = 2; i < n / 2; i++)
    {
        if (n % i == 0)
            cnt++;
    }
    return cnt == 0;
}

void dfs(vector<int> nums, int tot, int depth)
{
    if (depth >= 3)
    {
        if (isPrime(tot))
            ans++;
        return;
    }
    for (int i = 0; i < nums.size(); i++)
    {
        if (!visited[i] && depth < 3)
        {
            visited[i] = true;
            dfs(nums, tot + nums[i], depth + 1);
            visited[i] = false;
        }
    }
}
int solution(vector<int> nums)
{

    dfs(nums, 0, 0);

    return ans / 6;
}