#include <string>
#include <vector>

using namespace std;

int wall0[105][105] = {0, };
int wall1[105][105] = {0, };

bool check0(int x, int y)
{
    if (y == 2 || wall0[x][y-1] == 1 || wall1[x][y] == 1 || wall1[x-1][y] == 1)
    {
        return true;
    }
    return false;
}

bool check1(int x, int y)
{
    if (wall0[x][y-1] == 1 || wall0[x+1][y-1] == 1 || (wall1[x-1][y] == 1 && wall1[x+1][y] == 1))
    {
        return true;
    }
    return false;
}

bool canDelete(int x, int y)
{
    for (int i = x - 1; i <= x + 1; i++)
    {
        for (int j = y; j <= y + 1; j++)
        {
            if ((wall0[i][j] == 1 && !check0(i, j)) ||
           (wall1[i][j] == 1 && !check1(i, j)))
            {
                return false;
            }
        }
    }
    return true;
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
    vector<vector<int>> answer;
        
    for (vector<int> bf : build_frame)
    {
        int x = bf[0]+2;
        int y = bf[1]+2;
        int a = bf[2];
        int b = bf[3];
        
        if (b == 1)
        {
            if (a == 0)
            {
                if (check0(x, y))
               {
                    wall0[x][y] = 1;
               } 
            }
            else
            {
                if (check1(x, y))
                {
                   wall1[x][y] = 1;
                } 
            }
        }
        else
        {
            if (a == 0)
            {
                wall0[x][y] = 0;
                if (!canDelete(x, y))
                {
                    wall0[x][y] = 1;
                } 
            }
            else
            {
                wall1[x][y] = 0;
                if (!canDelete(x, y))
                {
                    wall1[x][y] = 1;
                } 
            }
        }
    }
   
    for (int i = 2; i <= n + 2; i++)
    {
        for (int j = 2; j <= n + 2; j++)
        {
            if (wall0[i][j] == 1)
            {
                answer.push_back({i-2, j-2, 0});
            }
            if (wall1[i][j] == 1)
            {
                answer.push_back({i-2, j-2, 1});
            }
        }
    }
    
    
    return answer;
}