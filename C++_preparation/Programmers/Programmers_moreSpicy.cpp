#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
typedef long long ll;

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;
    priority_queue<ll, vector<ll>, greater<ll> > pq;
    for (int i = 0; i < scoville.size(); i++)
    {
        pq.push(scoville[i]);
    }
    while (!pq.empty())
    {
        long long tmp = pq.top();
        pq.pop();
        if (tmp < K)
        {
            if (pq.size() >= 1)
            {
                long long mix = pq.top();
                pq.pop();
                pq.push(((mix * 2) + tmp));
                answer++;
            }
            else if (pq.size() == 0 && tmp < K)
            {
                return -1;
            }
        }
    }
    return answer;
}