#include <string>
#include <vector>

using namespace std;
int cnt = 0;

void dfs(vector<int> numbers, int target, int total, int depth)
{
    if (depth == numbers.size())
    {
        if (target == total)
            cnt++;
        return;
    }
    dfs(numbers, target, total + numbers[depth], depth + 1);
    dfs(numbers, target, total - numbers[depth], depth + 1);
}
int solution(vector<int> numbers, int target)
{
    dfs(numbers, target, 0, 0);
    int answer = cnt;
    return answer;
}