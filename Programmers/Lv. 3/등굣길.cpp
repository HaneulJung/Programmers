#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<int>> dp;
    for (int i = 0; i < n+1; i++)
    {
        vector<int> tmp;
        for (int j = 0; j < m+1; j++)
        {
            tmp.push_back(0);
        }
        dp.push_back(tmp);
    }
    dp[1][1] = 1;
    
    for (auto puddle : puddles)
    {
        dp[puddle[1]][puddle[0]] = -1;
    }
    
    for (int y = 1; y < n+1; y++)
    {
        for (int x = 1; x < m+1; x++)
        {
            if (x == 1 && y == 1)
            {
                continue;
            }
            
            if (dp[y][x] == -1)
            {
                dp[y][x] = 0;
            }
            else
            {
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007;
            }
        }
    }
    
    return dp[n][m];
}