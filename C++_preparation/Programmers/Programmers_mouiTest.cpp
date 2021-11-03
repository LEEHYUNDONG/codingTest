#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers)
{
    vector<int> answer = {0, 0, 0};
    vector<int> ans2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> ans3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> res;
    for (int i = 0; i < answers.size(); i++)
    {
        if (ans2[i % 8] == answers[i])
            answer[1]++;
        if (answers[i] == (i % 5) + 1)
            answer[0]++;
        if (ans3[i % 10] == answers[i])
            answer[2]++;
    }

    int max = *max_element(answer.begin(), answer.end()) - 1;
    for (int i = 0; i < 3; i++)
    {
        if (max < answer[i])
            res.push_back(i + 1);
    }
    return res;
}