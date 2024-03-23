#include <string>
#include <vector>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
  
    vector<vector<int>> distances(n+1, vector<int>(n+1, 20000001));
    for (int i = 1; i < n+1; i++)
    {
        distances[i][i] = 0;
    }
    
    for (vector<int> fare : fares)
    {
        int n1 = fare[0];
        int n2 = fare[1];
        int distance = fare[2];
        
        distances[n1][n2] = distance;
        distances[n2][n1] = distance;
    }
    
    for (int k = 1; k < n+1; k++)
    {
        for (int i = 1; i < n+1; i++)
        {
            for (int j = 1; j < n+1; j++)
            {
                if (distances[i][k] + distances[k][j] < distances[i][j])
                {
                    distances[i][j] = distances[i][k] + distances[k][j];
                }
            }
        }
    }
    
    int answer = 20000001;
    for (int i = 1; i < n+1; i++)
    {
        answer = min(answer, distances[s][i] + distances[i][a] + distances[i][b]);
    }
    
    return answer;
}


#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> Dijkstra(vector<vector<int>> distances, int start, int n)
{
    vector<int> dp(n+1, 20000001);
    
    priority_queue<pair<int, int>> pq;
    
    pq.push({start, 0});
    dp[start] = 0;
    
    while (!pq.empty())
    {
        int node = pq.top().first;
        int dis = -pq.top().second;
        pq.pop();
        
        for (int i = 1; i < n+1; i++)
        {
            if (distances[node][i] == 0)    continue;
            
            if (dis + distances[node][i] < dp[i])
            {
                dp[i] = dis + distances[node][i];
                pq.push({i, -dp[i]});
            }
        }
    }
    
    return dp;
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
  
    vector<vector<int>> distances(n+1, vector<int>(n+1, 0));    
    for (vector<int> fare : fares)
    {
        int n1 = fare[0];
        int n2 = fare[1];
        int distance = fare[2];
        
        distances[n1][n2] = distance;
        distances[n2][n1] = distance;
    }
    
    auto StoI = Dijkstra(distances, s, n);
    auto AtoI = Dijkstra(distances, a, n);
    auto BtoI = Dijkstra(distances, b, n);
    
    int answer = 20000001;
    for (int i = 1; i < n+1; i++)
    {
        answer = min(answer, StoI[i] + AtoI[i] + BtoI[i]);
    }
    
    return answer;
}