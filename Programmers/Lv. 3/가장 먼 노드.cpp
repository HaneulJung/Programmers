#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    vector<int> distances;
    vector<bool> visited;
    map<int, vector<int>> maps;
    for (int i = 0; i < n+1; i++)
    {
        distances.push_back(0);
        
        visited.push_back(false);
        
        maps[i] = {};
    }    
    visited[1] = true;
    
    for (vector<int> e : edge)
    {
        maps[e[0]].push_back(e[1]);
        maps[e[1]].push_back(e[0]);
    }
    
    queue<int> q;
    q.push(1);
    
    while (!q.empty())
    {
        int n = q.front();
        q.pop();
        
        for (int i : maps[n])
        {
            if (!visited[i])
            {
                visited[i] = true;
                
                distances[i] = distances[n] + 1;
                
                q.push(i);
            }
        }    
    }
    
    int m = *max_element(distances.begin(), distances.end());
    
    return count(distances.begin(), distances.end(), m);
}