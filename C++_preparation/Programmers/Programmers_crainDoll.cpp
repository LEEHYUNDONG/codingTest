#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int> > board, vector<int> moves)
{
    int answer = 0;
    vector<int> st;
    int b_size = board.size() - 1;

    for (int i = 0; i < moves.size(); i++)
    {
        int res = 0;
        for (int j = 0; j <= b_size; j++)
        {
            res = board[j][moves[i] - 1];
            if (res != 0)
            {
                board[j][moves[i] - 1] = 0;
                break;
            }
        }
        if (res == 0)
            continue;
        st.push_back(res);
    }
    if (st.size() == 1)
        return 0;
    for (int i = 0; i < st.size() - 1; i++)
    {
        if (st[i] == st[i + 1])
        {
            if (i > 0)
                st.erase(st.begin() + i, st.begin() + i + 2);
            else
                st.erase(st.begin(), st.begin() + 1);
            if (i == 0)
                i = -1;
            else
                i -= 2;
            answer += 2;
        }
    }
    return answer;
}