#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

int moveY[4] = {1, -1, 0, 0};
int moveX[4] = {0, 0, 1, -1};

int solution(vector<vector<int>> land) {
    int answer = 0;
    
    int sizeY = land.size();
    int sizeX = land[0].size();
    
    vector<int> line(sizeX);
    
    for (int y = 0; y < sizeY; y++)
    {
        for (int x = 0; x < sizeX; x++)
        {
            if (land[y][x] == 1)
            {
                land[y][x] = -1;
                
                queue<pair<int, int>> q;   // y, x
                q.push({y, x});
                
                set<int> xs;
                int cnt = 0;
                while (!q.empty())
                {
                    auto tmp = q.front();
                    q.pop();
                    
                    int cy = tmp.first;
                    int cx = tmp.second;
                    cnt++;
                    
                    xs.insert(cx);
                    
                    for (int i = 0; i < 4; i++)
                    {
                        int ny = cy + moveY[i];
                        int nx = cx + moveX[i];
                        
                        if (ny >= 0 && ny < sizeY && nx >= 0 && nx < sizeX && land[ny][nx] == 1)
                        {
                            land[ny][nx] = -1;
                            
                            q.push({ny, nx});
                        }
                    }
                }
                for (int s : xs)
                {
                    line[s] += cnt;
                }
            }
        }
    }
    
    return *max_element(line.begin(), line.end());
}