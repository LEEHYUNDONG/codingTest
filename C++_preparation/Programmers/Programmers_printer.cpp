#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int, int>> q;
    priority_queue<int> pq;
    
    for(int i = 0;i < priorities.size();i++){
        q.push({i, priorities[i]});
        pq.push(priorities[i]);
    }
    while(!q.empty()){
        int x = q.front().first;
        int v = q.front().second;
        q.pop();
        if(pq.top() == v){
            ++answer;
            pq.pop();
            if(location == x){
                return answer;
            }
        }else{
            q.push({x, v});
        }
    }
}