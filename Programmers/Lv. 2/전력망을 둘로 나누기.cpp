#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool IsIncluded(set<int> s, int i)
{
    auto iter = find(s.begin(), s.end(), i);
    return iter != s.end();
}

int solution(int n, vector<vector<int>> wires) {
    
    int m = 100;
    for (int w = 0; w < wires.size(); w++)
    {
        vector<vector<int>> new_wires(wires);
        new_wires.erase(new_wires.begin() + w);
        
        set<int> s1;
        s1.insert(new_wires[0][0]);
        s1.insert(new_wires[0][1]);
                
        bool checked[100] = {false, };
        
        int i = 1;
        while (i < new_wires.size())
        {                        
            if (!checked[i] && 
                (IsIncluded(s1, new_wires[i][0]) || IsIncluded(s1, new_wires[i][1])))
            {
                checked[i] = true;
                
                s1.insert(new_wires[i][0]);
                s1.insert(new_wires[i][1]);    
                
                i = 1;    
                continue;
            }
            i++;
        }       
        
        int a = max({s1.size(), n - s1.size()});
        int b = min({s1.size(), n - s1.size()});
        
        m = min({ m,  a - b });
    }    
    
    return m;
}