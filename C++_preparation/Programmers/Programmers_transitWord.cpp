#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <memory.h>

using namespace std;

bool visited[50];
int answer = 1000;

void dfs(vector<string> words, string begin, string target, int depth)
{
    if (target == begin)
    {
        answer = min(depth, answer);
        return;
    }
    else if (depth >= words.size())
        return;

    for (int i = 0; i < words.size(); i++)
    {
        int cnt = 0;
        for (int j = 0; j < begin.size(); j++)
        {
            if (words[i][j] != begin[j])
                cnt++;
            if (cnt >= 2)
                break;
        }
        if (cnt == 1 && !visited[i])
        {
            visited[i] = true;
            dfs(words, words[i], target, depth + 1);
            visited[i] = false;
        }
    }
}
int solution(string begin, string target, vector<string> words)
{
    // if(find(words.begin(), words.end(), target) == words.end()) return 0;
    memset(visited, false, sizeof(visited));
    dfs(words, begin, target, 0);
    if (answer == 1000)
        return 0;
    else
        return answer;
}