#include <string>
#include <vector>
#include <map>
#include <tuple>

using namespace std;

map<int, vector<int>> connected;
vector<int> info_copy;
bool visited[18][18][18] = {false, };

int max_sheep = 1;

void dfs(int node, int sheep, int wolf)
{
    if (wolf >= sheep)
    {
        return;
    }
    
    max_sheep = max(max_sheep, sheep);
    
    for (int next : connected[node])
    {
        if (info_copy[next] == 0 && !visited[next][sheep+1][wolf])
        {
            visited[next][sheep+1][wolf] = true;
            info_copy[next] = -1;

            dfs(next, sheep+1, wolf);
            
            visited[next][sheep+1][wolf] = false;
            info_copy[next] = 0;
        }
        else if (info_copy[next] == 1)
        {
            if (sheep > wolf + 1 && !visited[next][sheep][wolf+1])   
            {
                visited[next][sheep][wolf+1] = true;
                info_copy[next] = -1;
                
                dfs(next, sheep, wolf+1);
                
                visited[next][sheep][wolf+1] = false;
                info_copy[next] = 1;
            }
        }
        else
        {
            if (!visited[next][sheep][wolf])
            {
                visited[next][sheep][wolf] = true;
                
                dfs(next, sheep, wolf);
                
                visited[next][sheep][wolf] = false;
            }
        }
    }    
}

int solution(vector<int> info, vector<vector<int>> edges) {
    for (vector<int> edge : edges)
    {
        connected[edge[0]].push_back(edge[1]);
        connected[edge[1]].push_back(edge[0]);
    }
    
    visited[0][1][0] = true;
    info_copy = info;
    info_copy[0] = -1;
    
    dfs(0, 1, 0);
    
    return max_sheep;
}