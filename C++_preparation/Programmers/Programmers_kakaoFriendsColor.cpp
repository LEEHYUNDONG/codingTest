#include <vector>
#include <deque>
#include <iostream>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int> > picture)
{
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    deque<pair<int, int> > q;
    int visited[101][101] = {0};
    int direction[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};

    int color;
    int cnt = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                q.push_front(make_pair(i, j));
                visited[i][j] = 1;
                color = picture[i][j];
                cnt = 1;
                if (color != 0)
                    number_of_area++;
                while (!q.empty())
                {
                    int x = q[0].first;
                    int y = q[0].second;
                    q.pop_front();
                    color = picture[i][j];
                    for (int i = 0; i < 4; i++)
                    {
                        int rx = x + direction[i][0];
                        int ry = y + direction[i][1];
                        if (0 <= rx && rx < m && 0 <= ry && ry < n)
                        {
                            if (!visited[rx][ry] && color == picture[rx][ry])
                            {
                                visited[rx][ry] = 1;
                                q.push_front(make_pair(rx, ry));
                                if (color != 0)
                                {
                                    cnt += 1;
                                }
                            }
                        }
                    }
                }
                // cout << "color :" << color << "\n";
                // cout << "cnt :" << cnt << "\n";
                // cout << "number of area :" << number_of_area << "\n";
                max_size_of_one_area = max(cnt, max_size_of_one_area);
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}