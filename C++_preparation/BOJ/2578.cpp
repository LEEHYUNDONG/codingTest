#include <bits/stdc++.h>
#define SIZE 5
using namespace std;

int MAP[SIZE][SIZE];
int call[SIZE][SIZE];

void input()
{
    //input MAP
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE;j++){
            cin >> MAP[i][j];
        }
    }

    //input call
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE;j++){
            cin >> call[i][j];
        }
    }

    return;
}

// find number that mc calls
void eraseNum(int num){
    for (int i = 0; i < SIZE;i++){
        for (int j = 0; j < SIZE;j++){
            if(MAP[i][j] == num){
                MAP[i][j] = 0;
                return;
            }
        }
    }
}

bool findBingo()
{
    // cout << "----------------------------\n";
    // for (int i = 0; i < SIZE;i++){
    //     for (int j = 0; j < SIZE;j++){
    //         cout << MAP[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }
        int cnt = 0;
    for (int i = 0; i < SIZE; i++)
    {
        int cnt_row = 0;
        for (int j = 0; j < SIZE; j++)
        {
            if(MAP[i][j] == 0)
                cnt_row++;
        }
        if(cnt_row == 5)
            cnt++;
    }

    for (int i = 0; i < SIZE;i++){
        int cnt_col = 0;
        for (int j = 0; j < SIZE; j++)
        {
            if(MAP[j][i] == 0)
                cnt_col++;
        }
        if(cnt_col == 5)
            cnt++;
    }
    // cout << "cnt :" << cnt << '\n';
    int cnt_diag = 0, cnt_revdiag = 0;
    for (int i = 0; i < SIZE; i++)
    {
        if(MAP[i][i] == 0)
            cnt_diag++;
        if(MAP[4-i][i] == 0)
            cnt_revdiag++;
    }
    if(cnt_diag == 5)
        cnt++;
    if(cnt_revdiag == 5)
        cnt++;
    // cout << "cnt :" << cnt << '\n';
    
    if (cnt > 2)
        return true;
    return false;
}

int solve()
{
    int cnt = 0;
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE;j++){
            eraseNum(call[i][j]);
            cnt++;
            if (cnt >= 15 && findBingo())
                return cnt;
        }
    }
    return 0;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    //input data
    input();

    //solve
    cout << solve();

    return 0;
}