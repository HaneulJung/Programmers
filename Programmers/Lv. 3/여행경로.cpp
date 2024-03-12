#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>

using namespace std;

bool cmp(vector<string> a, vector<string> b)
{
    if (a[0] == b[0])
    {
        return a[1] < b[1];    
    }
    return a[0] < b[0];
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end(), cmp);
    
    vector<string> routes;
    routes.push_back("ICN");
    
    vector<bool> visited;
    for (int i = 0; i < tickets.size(); i++)
    {
        visited.push_back(false);
    }
    
    queue<tuple<string, vector<bool>, vector<string>>> q;
    q.push({"ICN", visited, routes});
    
    while(!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        
        
        string depart = get<0>(tmp);
        vector<bool> visited_tmp;
        vector<string> routes_tmp;
        
        if (get<2>(tmp).size() == tickets.size() + 1)
        {            
            return get<2>(tmp);
        }
        
        for (int i = 0; i < tickets.size(); i++)
        { 
            visited_tmp = get<1>(tmp);
            routes_tmp = get<2>(tmp);
            
            if (!visited_tmp[i] && tickets[i][0] == depart)
            {
                visited_tmp[i] = true;
                routes_tmp.push_back(tickets[i][1]);
                q.push({tickets[i][1], visited_tmp, routes_tmp});
            }
        }
    }       
    
    return {"ICN"};
}