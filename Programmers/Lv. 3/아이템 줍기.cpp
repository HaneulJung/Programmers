#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    int x_move[4] = {0, 0, 1, -1};
    int y_move[4] = {1, -1, 0, 0};
    
    int max_x = 0, max_y = 0;
    
    vector<vector<int>> box;    
    vector<vector<bool>> visited;    
    
    for (vector<int> rec : rectangle)
    {
        if (rec[2] > max_x)
        {
            max_x = rec[2];
        }
        if (rec[3] > max_y)
        {
            max_y = rec[3];
        }
    }
    
    for (int x = 0; x < 2*max_x + 1; x++)
    {
        vector<int> tmp;
        vector<bool> tmp2;
        for (int y = 0; y < 2*max_y + 1; y++)
        {
            tmp.push_back(0);
            tmp2.push_back(false);
        }
        box.push_back(tmp);
        visited.push_back(tmp2);
    }
    
    for (vector<int> rec : rectangle)
    {
        int x1 = 2*rec[0];
        int y1 = 2*rec[1];
        int x2 = 2*rec[2];
        int y2 = 2*rec[3];
        for (int x = x1 + 1; x < x2; x++)
        {
            for (int y = y1 + 1; y < y2; y++)
            {
                box[x][y] = -1;                
            }
        }
    }
    
    for (vector<int> rec : rectangle)
    {
        int x1 = 2*rec[0];
        int y1 = 2*rec[1];
        int x2 = 2*rec[2];
        int y2 = 2*rec[3];
        for (int x = x1; x < x2 + 1; x++)
        {
            for (int y = y1; y < y2 + 1; y++)
            {
                if (box[x][y] != -1)
                {
                    box[x][y] = 1;                    
                }                
            }
        }
    }       
    
    queue<vector<int>> q;
    q.push({2*characterX, 2*characterY, 0});
    while (!q.empty())
    {
        vector<int> tmp = q.front();
        q.pop();
        int cx = tmp[0];
        int cy = tmp[1];
        int cnt = tmp[2];
        
        if (cx == 2*itemX && cy == 2*itemY)
        {
            return int(cnt/2);
        }
        
        for (int i = 0; i < 4; i++)
        {
            int nx = cx + x_move[i];
            int ny = cy + y_move[i];
            
            if (nx >= 0 && nx <= 2*max_x && ny >= 0 && ny <= 2*max_y && box[nx][ny] == 1 && !visited[nx][ny])
            {
                visited[nx][ny] = true;
                q.push({nx, ny, cnt+1});
            }
        }
    }
    
    return answer;
}