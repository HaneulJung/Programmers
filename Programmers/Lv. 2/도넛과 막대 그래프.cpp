#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

vector<int> solution(vector<vector<int>> edges) {
    vector<int> answer;
    
    map<int, vector<int>> m;
    
    set<int> in_nodes;
    set<int> out_nodes;
    
    for (vector<int> edge : edges)
    {
        m[edge[0]].push_back(edge[1]);
        in_nodes.insert(edge[1]);
        
        if (m[edge[0]].size() >= 2)
        {
            out_nodes.insert(edge[0]);
        }
    }
    
    int start_node = 0;
    for (int n : out_nodes)
    {
        if (in_nodes.find(n) == in_nodes.end())
        {
            start_node = n;
            break;
        }
    }
    
    int doughnut = 0, stick = 0, eight = 0;
    for (int n : m[start_node])
    {
        set<int> nodes;
        nodes.insert(n);
        int line_cnt = 0;
        int cur_node = n;
        bool pass = false;
        
        while (m[cur_node].size() > 0)
        {
            if (m[cur_node].size() == 2)
            {
                eight++;
                pass = true;
                break;
            }
            
            int tmp = m[cur_node].back();
            m[cur_node].pop_back();
            cur_node = tmp;
            
            nodes.insert(tmp);
            line_cnt++;
        }
        
        if (!pass)
        {
            if (nodes.size() == line_cnt)
            {
                doughnut++;
            }
            else if (nodes.size() + 1 == line_cnt)
            {
                eight++;
            }
            else
            {
                stick++;
            }            
        }
    }
    
    return {start_node, doughnut, stick, eight};
}