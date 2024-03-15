#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int directions[8][2] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, 
                        {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

int solution(vector<int> arrows) {
    int answer = 0;
    
    map<pair<int, int>, bool> visited;
    map<pair<pair<int, int>, pair<int, int>>, bool> line;
        
    int cx = 0, cy = 0;
    visited[{cx, cy}] = true;
    
    for (int i = 0; i < arrows.size(); i++)
    {       
        for (int j = 0; j < 2; j++)
        {
            int nx = cx + directions[arrows[i]][0];
            int ny = cy + directions[arrows[i]][1];    
            
            if (visited[{nx, ny}] && !line[{{cx, cy}, {nx, ny}}])
            {
                answer++;
            }
            
            visited[{nx, ny}] = true;
            line[{{cx, cy}, {nx, ny}}] = true;
            line[{{nx, ny}, {cx, cy}}] = true;
            
            cx = nx;
            cy = ny;
        }
        
    }
    
    return answer;
}