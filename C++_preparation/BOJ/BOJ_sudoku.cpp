#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;

int sudoku[9][9];
bool visited[9][9];

int main()
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> sudoku[i][j];
        }
    }
    return 0;
}