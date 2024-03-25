#include <string>
#include <vector>
#include <queue>
#include <map>

#define INF 10000000

using namespace std;

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
        
    vector<int> dp(n+1, INF);
    dp[destination] = 0;
        
    map<int, vector<int>> routes;
    for (vector<int> road : roads)
    {
        routes[road[0]].push_back(road[1]);
        routes[road[1]].push_back(road[0]);
    }
    
    vector<bool> visited(n+1, false);
    visited[destination] = true;
    queue<pair<int, vector<bool>>> q;
    q.push({destination, visited});
    
    while (!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        
        int node = tmp.first;
        auto visited_tmp = tmp.second;
        
        for (int r : routes[node])
        {
            if (!visited_tmp[r])
            {
                visited_tmp[r] = true;
                
                if (dp[r] > dp[node] + 1)
                {
                    dp[r] = dp[node] + 1;
                    q.push({r, visited_tmp});
                }
                
                visited_tmp[r] = false;
            }
        }
    }
    
    for (int s : sources)
    {
        if (dp[s] == INF)
        {
            answer.push_back(-1);
        }
        else
        {
            answer.push_back(dp[s]);
        }
    }
    
    return answer;
}