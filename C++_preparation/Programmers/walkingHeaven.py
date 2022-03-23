#include <vector>
#include <iostream>

using namespace std;

int MOD = 20170805;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    int dp[501][501][2] = {0};
    
    for (int i = 0;i < m;i++){
        if (city_map[i][0] == 0 or city_map[i][0] == 2){
            dp[i][0][1] = 1; // 위쪽
        }else{
            break;
        }
    }
    for (int i = 0;i < n;i++){
        if (city_map[0][i] == 0 or city_map[0][i] == 2){
            dp[0][i][0] = 1; // 왼
        }else
            break;
        
    }
    for (int i = 1;i < m;i++){
        for (int j = 1;j < n;j++){
            if(city_map[i-1][j] == 0) 
                dp[i][j][1] += (dp[i-1][j][0] + dp[i-1][j][1]) % MOD;
            if(city_map[i-1][j] == 2) 
                dp[i][j][1] += (dp[i-1][j][1] % MOD);
            
            if(city_map[i][j-1] == 0) 
                dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][1]) % MOD;

            if(city_map[i][j-1] == 2) 
                dp[i][j][0] += (dp[i][j-1][0] % MOD);
            
        }
    }
    
    return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD;
}