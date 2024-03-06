#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int solution(vector<vector<int>> maps)
{
    queue<tuple<int, int, int>> q;
    
    bool visited[100][100] = {false, };
    
    int x_move[4] = {1, -1, 0, 0};
    int y_move[4] = {0, 0, 1, -1};
    
    int x_pos = 0;
    int y_pos = 0;
    int cnt = 1;
    
    int x_des = maps[0].size() - 1;
    int y_des = maps.size() - 1;
    
    q.push({y_pos, x_pos, cnt});
    
    while (!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        
        int c_y_pos = get<0>(tmp);
        int c_x_pos = get<1>(tmp);
        int c_cnt = get<2>(tmp);
        
        if (c_y_pos == y_des && c_x_pos == x_des)
        {
            return c_cnt;
        }
        
        for (int i = 0; i < 4; i++)
        {
            int n_y_pos = c_y_pos + y_move[i];
            int n_x_pos = c_x_pos + x_move[i];
            
            if ((0 <= n_y_pos && n_y_pos <= y_des) && 
                (0 <= n_x_pos && n_x_pos <= x_des) && 
                !visited[n_y_pos][n_x_pos] &&
                maps[n_y_pos][n_x_pos] != 0)
            {
                visited[n_y_pos][n_x_pos] = true;
                
                q.push({n_y_pos, n_x_pos, c_cnt+1});
            }
        }
    }
    
    return -1;
}