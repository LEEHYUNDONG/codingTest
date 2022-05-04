#include <string>
#include <vector>
#include <algorithm>
using namespace std;

/*
* 응시자 p , 빈테이블 O, 파티션 X
*/
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
bool visited[6][6] = {false};
bool flag;
vector<int> answer;

void dfs(int x, int y, vector<string> graph, int depth)
{
    if (depth >= 2){
        return;
    }
    for (int i = 0;i < 4;i++){
        int rx = x + dx[i];
        int ry = y + dy[i];
        if(0<=rx && rx < 5 && ry >= 0 && ry < 5 && !visited[rx][ry]){
            if (graph[rx][ry] != 'X'){
                if (graph[rx][ry] == 'P')
                    flag = true;
                visited[rx][ry] = true;
                dfs(rx, ry, graph, depth+1);
            }
        }
    }
}
vector<int> solution(vector<vector<string>> places) {
    for (int p = 0;p < places.size();p++){
        fill(&visited[0][0], &visited[5][5], false);
        flag = false;
        for (int i = 0;i < 5;i++){
            for (int j = 0;j < 5;j++){
                if(places[p][i][j] == 'P' && !visited[i][j]){
                    visited[i][j] = true;
                    dfs(i, j, places[p], 0);
                }
            }
        }
        
        if (flag)
            answer.push_back(0);
        else
            answer.push_back(1);
    }
    
    return answer;
}