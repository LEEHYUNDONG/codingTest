#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;
typedef long long ll;

int solution(vector<int> queue1, vector<int> queue2) {
    ll answer = 0;
    ll tot = 0, tot1 = 0, tot2 = 0;
    ll l = queue1.size();
    queue<ll> q1, q2;
    
    for(auto a : queue1){
        q1.push(a);
        tot1 += a;
    }
    for(auto a : queue2){
        q2.push(a);
        tot2 += a;
    }
    
    
    while(tot1 != tot2){
        if(answer >= l*3){
            answer = -1;
            break;
        }
            
        if(tot1 < tot2){
            tot1 += q2.front();
            tot2 -= q2.front();
            q1.push(q2.front());
            q2.pop();
            
        }else if(tot1 > tot2){
            tot2 += q1.front();
            tot1 -= q1.front();
            q2.push(q1.front());
            q1.pop();
        }
        answer++;
    }
    
    return answer;
}