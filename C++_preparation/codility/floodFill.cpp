// you can use includes, for example:
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    queue<int> q;
    int size = A.size();
    int ans = 0;
    int maxH = find(A.begin(), A.end(), *max_element(A.begin(), A.end())) - A.begin();
    int rh = 0;
    
    for (int i = 0;i < maxH;i++){
        if (rh < A[i])
            rh = A[i];
        else
            ans = max(ans, (rh-A[i]));
    }
    rh = A[size-1];
    
    for (int i = size-1;i > maxH;i--){
        if (rh < A[i])
            rh = A[i];
        else
            ans = max(ans, (rh-A[i]));
    }
    return ans;
}