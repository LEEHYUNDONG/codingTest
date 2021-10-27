#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool isDist(int num, int dist, char ope)
{
    if (ope == '=')
        return (num == dist);
    else if (ope == '<')
        return (num < dist);
    else if (ope == '>')
        return (num > dist);
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data)
{
    int answer = 0;
    string s = "ACFJMNRT";

    do
    {
        bool flag = true;
        for (int i = 0; i < data.size(); i++)
        {
            char ff = data[i][0];
            char sf = data[i][2];
            char op = data[i][3];
            int dist = int(data[i][4]) - '0';
            int fl = find(s.begin(), s.end(), ff) - s.begin();
            int sl = find(s.begin(), s.end(), sf) - s.begin();
            if (isDist(abs(fl - sl) - 1, dist, op))
                continue;
            flag = false;
        }
        if (flag)
           answer++;

    } while (next_permutation(s.begin(), s.end()));
    return answer;
}