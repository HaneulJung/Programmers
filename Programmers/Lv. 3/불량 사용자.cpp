#include <string>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> v;
set<set<int>> ss;

void dfs(set<int> s, int depth)
{
    if (depth == v.size())
    {
        if (s.size() == depth)
        {
            ss.insert(s);
        }
        return;
    }
    
    for (int vv : v[depth])
    {
        set<int> tmp_s = s;
        tmp_s.insert(vv);
        dfs(tmp_s, depth+1);
    }
}

int solution(vector<string> user_id, vector<string> banned_id) {
    for (int i = 0; i < banned_id.size(); i++)
    {
        vector<int> tmp;
        for (int j = 0; j < user_id.size(); j++)
        {            
            if (banned_id[i].size() == user_id[j].size())
            {                
                bool isRight = true;
                for (int k = 0; k < user_id[j].size(); k++)
                {
                    if (banned_id[i][k] != '*' && banned_id[i][k] != user_id[j][k])
                    {
                        isRight = false;
                        break;
                    }
                }
                if (isRight)
                {
                    tmp.push_back(j);
                }
            }
        }
        v.push_back(tmp);
    }
    
    set<int> s;
    dfs(s, 0);
    
    return ss.size();
}