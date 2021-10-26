#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

int solution(vector<string> lines)
{
    double d;
    int answer = 0;
    vector<string> dl(2001);
    vector<int> starttime(2001), endtime(2001);

    if (lines.size() == 1)
    {
        return 1;
    }
    for (int i = 0; i < lines.size(); i++)
    {
        stringstream ss;
        for (int j = 0; j < lines[i].length(); j++)
        {
            if (lines[i][j] == '-' || lines[i][j] == ':' || lines[i][j] == 's')
            {
                lines[i][j] = ' ';
            }
        }
        lines[i].erase(lines[i].begin(), lines[i].begin() + 11);
        ss << lines[i];
        float d;
        float tmp = 0.0;
        int cnt = 0;
        while (ss >> d)
        {
            if (cnt == 0)
                tmp += 60 * 60 * d;
            else if (cnt == 1)
                tmp += 60 * d;
            else
                tmp += d;
            cnt++;
        }
        time[i] = tmp;
    }
    for (int i = 0; i < lines.size(); i++)
    {
        cout << time[i] << endl;
    }

    return answer;
}
int main()
{

    return 0;
}