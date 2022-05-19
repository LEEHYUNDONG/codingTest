#include <bits/stdc++.h>
using namespace std;

int arr[100001];
int N, M;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int l, r = 0;
    cin >> N >> M;

    for (int i = 0; i < N;i++){
        cin >> arr[i];
        r += arr[i];
    }
    l = *max_element(arr, arr + N);

    while (l <= r){
        int mid = (l + r) / 2;
        int tot = 0, cnt = 0;
        for (int i = 0; i < N;i++){
            if (tot + arr[i] > mid){
                tot = 0;
                cnt++;
            }
            tot += arr[i];
        }
        
        if(tot != 0)
            cnt++;

        if (cnt > M)
            l = mid + 1;
        else
            r = mid - 1;
    }
    cout << l;
    return 0;
}