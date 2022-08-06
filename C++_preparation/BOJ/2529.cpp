#include <bits/stdc++.h>
using namespace std;

int K;
char op[10];
vector<string> ans;
vector<char> tmp;
bool visited[10];

void dfs(int depth, int num)
{
    if(depth == K+1){
        string ttmp = "";
        for (int i = 0; i < K + 1;i++){
            ttmp += tmp[i];
        }
        ans.push_back(ttmp);
        return;
    }
    
    for (int j = num+1; j < 10;j++){
        if(((op[depth] == '<') && (num < j)) || ((op[depth] == '>') && (num > j))){
            tmp.push_back('0'+j);
            visited[depth] = true;
            dfs(depth + 1, j);
            visited[depth] = false;
            tmp.pop_back();    
        }
    }
}

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    //init
    fill(&visited[0], &visited[9], false);
    cin >> K;
    for (int i = 0; i < K;i++){
        cin >> op[i];
    }
    for (int i = 0; i <= 9;i++){
        tmp.push_back(i);
        dfs(0, i);
        tmp.pop_back();
    }
    for(auto a : ans)
        cout << a << '\n';

    return 0;
}