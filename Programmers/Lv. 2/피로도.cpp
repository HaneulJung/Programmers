#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int cnt = 0;

void dfs(vector<vector<int>> dungeons, bool *visited, int cur_h, int depth)
{
    if (depth == dungeons.size())
    {
        cnt = depth;
        return;
    }
    if (cur_h < 0)
    {
        cnt = max({cnt, depth-1});
        return;
    }
    
    for (int i = 0; i < dungeons.size(); i++)
    {
        if (!visited[i])
        {            
            visited[i] = true;
            
            int new_h;
            if (cur_h >= dungeons[i][0])
            {                
                new_h = cur_h - dungeons[i][1];  
                
                dfs(dungeons, visited, new_h, depth+1);
            }
            else
            {
                cnt = max({cnt, depth});
            }                
            visited[i] = false;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    bool visited[8] = {false, };
    
    dfs(dungeons, visited, k, 0);
    
    return cnt;
}