#include <string>
#include <vector>

using namespace std;

int solution(string numbers)
{
    int answer = 0;
    return answer;
}
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int visited[8];
string s = "";
vector<int> nums;

bool isPrime(int x)
{
    if (x < 2)
        return false;

    for (int i = 2; i <= sqrt(x); i++)
    {
        if ((x % i) == 0)
            return false;
    }
    return true;
}

// void dfs(string numbers, int ind, int depth)
// {
//     if(depth == numbers.length())
//         return;
//     for(int i = 0;i < numbers.length();i++){
//         if(!visited[i]){
//             s += numbers[i];
//             visited[i] = true;
//             // if(num.empty() || find(num.begin(), num.end(), stoi(s)) == num.end()){
//             num.push_back(stoi(s));
//             // }
//             dfs(numbers, i, depth+1);
//             visited[i] = false;
//         }
//     }
//     s = "";
// }
int solution(string numbers)
{
    int answer = 0;
    vector<char> v;

    for (int i = 0; i < numbers.size(); i++)
        v.push_back(numbers[i]);
    sort(v.begin(), v.end());
    sort(v.begin(), v.end());
    // dfs(numbers, 0, 0);
    do
    {
        string temp = ""; // 만들 수 있는 모든 숫자 nums에 저장
        for (int i = 0; i < v.size(); i++)
        {
            temp.push_back(v[i]);
            nums.push_back(stoi(temp));
        }
    } while (next_permutation(v.begin(), v.end()));

    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    for (int i = 0; i < nums.size(); i++)
    {
        // cout << a << '\n';
        if (isPrime(nums[i]))
        {
            answer++;
        }
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

        int visited[8];
        string s = "";
        vector<int> nums;

        bool isPrime(int x)
        {
            if (x < 2)
                return false;

            for (int i = 2; i <= sqrt(x); i++)
            {
                if ((x % i) == 0)
                    return false;
            }
            return true;
        }

        // void dfs(string numbers, int ind, int depth)
        // {
        //     if(depth == numbers.length())
        //         return;
        //     for(int i = 0;i < numbers.length();i++){
        //         if(!visited[i]){
        //             s += numbers[i];
        //             visited[i] = true;
        //             // if(num.empty() || find(num.begin(), num.end(), stoi(s)) == num.end()){
        //             num.push_back(stoi(s));
        //             // }
        //             dfs(numbers, i, depth+1);
        //             visited[i] = false;
        //         }
        //     }
        //     s = "";
        // }
        int solution(string numbers)
        {
            int answer = 0;
            vector<char> v;

            for (int i = 0; i < numbers.size(); i++)
                v.push_back(numbers[i]);
            sort(v.begin(), v.end());
            sort(v.begin(), v.end());
            // dfs(numbers, 0, 0);
            do
            {
                string temp = ""; // 만들 수 있는 모든 숫자 nums에 저장
                for (int i = 0; i < v.size(); i++)
                {
                    temp.push_back(v[i]);
                    nums.push_back(stoi(temp));
                }
            } while (next_permutation(v.begin(), v.end()));

            sort(nums.begin(), nums.end());
            nums.erase(unique(nums.begin(), nums.end()), nums.end());

            for (int i = 0; i < nums.size(); i++)
            {
                // cout << a << '\n';
                if (isPrime(nums[i]))
                {
                    answer++;
                }
            }
            return answer;
        }
    }
    return answer;
}