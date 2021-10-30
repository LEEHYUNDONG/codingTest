#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

int cnt[27]; // cnt[i]=n : 길이가 i인 조합 중 최대 주문 횟수는 n번
unordered_map<string, int> food_cnt;
vector<string> menu[27][21]; // i번 주문한 음식 j개

void combinationOfMenu(string s, int idx, string made)
{
    if (made.size() > 1)
    {
        food_cnt[made]++;
        cnt[made.size()] = max(cnt[made.size()], food_cnt[made]);
        menu[made.size()][food_cnt[made]].push_back(made);
    }
    for (int i = idx + 1; i < s.size(); i++)
    {
        made.push_back(s[i]);
        combinationOfMenu(s, i, made);
        made.pop_back();
    }
}
vector<string> solution(vector<string> orders, vector<int> course)
{
    vector<string> answer;
    for (string &s : orders)
    {
        sort(s.begin(), s.end());
        combinationOfMenu(s, -1, "");
    }

    // 쿼리 수행
    for (int i : course)
        if (cnt[i] > 1) // 길이가 i인 조합의 최대 주문 횟수가 1 이상인 경우만
            for (string s : menu[i][cnt[i]])
                answer.push_back(s);
    sort(answer.begin(), answer.end());
    return answer;
}