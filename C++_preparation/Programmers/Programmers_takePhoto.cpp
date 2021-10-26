#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<char> vec;
int visited[8] = {0};
vector<char> character = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int ans = 0;
int flag = 1;
int dfs(int depth, vector<string> data, char ch, int l){
    if(vec.size() == 8){
        int cnt = 0;
        // if (flag == 1){
        //     for(int i = 0;i < 8;i++)
        //         cout << vec[i] << " ";
        //     cout << "\n";
        //     int x = find(vec.begin(), vec.end(), data[0][0]) - vec.begin();
        //     int y = find(vec.begin(), vec.end(), data[0][2]) - vec.begin();
        //     int dist = abs(x-y);
        //     int redist = int(data[0][4])-'0';
        //     cout << "x, y, disf, redist :" << x << " " << y << " " << dist << " " <<redist << '\n';
        //     if(ans >5) flag = 0;
        // }
        for(int k = 0;k < l;k++){
            int x = find(vec.begin(), vec.end(), data[k][0]) - vec.begin();
            int y = find(vec.begin(), vec.end(), data[k][2]) - vec.begin();
            int dist = abs(x-y);
            int redist = int(data[k][4])-'0';
            if((data[k][3] == '=') && (dist == redist)){
                cnt++;
                continue;
            }else if((data[k][3] == '<') && (dist < redist)){
                cnt++;
                continue;
            }else if((data[k][3] == '>') && (dist > redist)){
                cnt++;
                continue;
            }
        }
        if(cnt == l){
            ++ans;
        }
        return 0;
    }
    for(int i = 0;i < 8;i++){
        if(visited[i] == 0 && ch != character[i]){
            vec.push_back(character[i]);
            visited[i] = 1;
            dfs(i+1, data, character[i], l);
            visited[i] = 0;
            vec.pop_back();
        }
    }
    return 1;
}
int solution(int n, vector<string> data) {
    int answer = 0;
    dfs(0, data, '0', data.size());
    answer = ans;
    return answer;
}