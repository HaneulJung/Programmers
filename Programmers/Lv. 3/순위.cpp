#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    
    map<int, vector<int>> win_maps;
    map<int, vector<int>> lose_maps;
    
    for (vector<int> result : results)
    {
        if (win_maps.count(result[0]) == 0)
        {
            win_maps[result[0]] = {};
        }
        win_maps[result[0]].push_back(result[1]);
        
        if (lose_maps.count(result[1]) == 0)
        {
            lose_maps[result[1]] = {};
        }
        lose_maps[result[1]].push_back(result[0]);
    }
    
    for (int i = 1; i < n + 1; i++)
    {
        queue<int> q;
        set<int> s;
                
        q.push(i);       
        while(!q.empty())
        {
            int c = q.front();
            q.pop();
            
            for (int n : win_maps[c])
            {                
                if (s.count(n) == 0 && n != i)
                {
                    s.insert(n);
                    
                    q.push(n);
                }
            }
        }
        
        q.push(i);
        while(!q.empty())
        {
            int c = q.front();
            q.pop();
            
            for (int n : lose_maps[c])
            {                
                if (s.count(n) == 0 && n != i)
                {
                    s.insert(n);
                    
                    q.push(n);
                }
            }
        }
        
        if (s.size() == n - 1)
        {
            answer++;
        }
    }
    
    return answer;
}