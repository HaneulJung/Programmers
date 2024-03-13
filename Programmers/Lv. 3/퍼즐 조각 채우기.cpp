#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int y_move[4] = {1, -1, 0, 0};
int x_move[4] = {0, 0, 1, -1};

vector<pair<int, int>> MoveToZero(vector<pair<int, int>> v)
{
    int min_Y = 51;
    int min_X = 51;
    
    for (pair<int, int> p : v)
    {
        if (p.first < min_Y)
        {
            min_Y = p.first;
        }
        if (p.second < min_X)
        {
            min_X = p.second;
        }
    }
        
    vector<pair<int, int>> new_v;
    sort(v.begin(), v.end());
    for (pair<int, int> p : v)
    {
        new_v.push_back({p.first - min_Y, p.second - min_X});
    }
    
    return new_v;
}

vector<vector<pair<int, int>>> FindShapes(vector<vector<int>> board, int num)
{
    vector<vector<pair<int, int>>> results;
    
    int size_Y = board.size();
    int size_X = board[0].size();
    
    bool visited[51][51] = {false, };
    
    
    for (int y = 0; y < size_Y; y++)
    {
        for (int x = 0; x < size_X; x++)
        {
            queue<pair<int, int>> q;       
            vector<pair<int, int>> v;     
            
            if (!visited[y][x] && board[y][x] == num)
            {
                visited[y][x] = true;
                
                v.push_back({y, x});
                q.push({y, x});
                
                while (!q.empty())
                {
                    auto tmp = q.front();
                    q.pop();
                    
                    int cy = tmp.first;
                    int cx = tmp.second;
                    
                    for (int i = 0; i < 4; i++)
                    {
                        int ny = cy + y_move[i];
                        int nx = cx + x_move[i];
                        
                        if (ny >= 0 && ny < size_Y && nx >= 0 && nx < size_X && !visited[ny][nx] && board[ny][nx] == num)
                        {
                            visited[ny][nx] = true;
                            
                            v.push_back({ny, nx});
                            
                            q.push({ny, nx});
                        }
                    }
                }                
                results.push_back(MoveToZero(v));
            }
        }
    }
    return results;
}

vector<vector<pair<int, int>>> RotateShapes(vector<pair<int, int>> board)
{
    vector<vector<pair<int, int>>> results;
    results.push_back(board);
    
    for (int i = 0; i < 3; i++)
    {
        vector<pair<int, int>> tmp_v;
        for (pair<int, int> p : board)
        {
            tmp_v.push_back({p.second, -p.first});
        }
        board = MoveToZero(tmp_v);
        results.push_back(board);
    }
    
    return results;
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    int answer = 0;
    
    vector<vector<pair<int, int>>> emptys = FindShapes(game_board, 0);
    vector<vector<pair<int, int>>> blocks = FindShapes(table, 1);
    
    vector<bool> used;
    for (int i = 0; i < blocks.size(); i++)
    {
        used.push_back(false);
    }
    
    for (int i = 0; i < emptys.size(); i++)
    {
        for (int j = 0; j < blocks.size(); j++)
        {            
            auto rotated = RotateShapes(blocks[j]);
            if (!used[j] && count(rotated.begin(), rotated.end(), emptys[i]) != 0)
            {               
                used[j] = true;
                answer += emptys[i].size();
                break;
            }
        }
    }
        
    return answer;
}