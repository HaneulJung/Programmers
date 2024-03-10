#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

bool CheckString(string s1, string s2)
{
    int cnt = 0;
    
    for (int i = 0; i < s1.length(); i++)
    {
        if (s1[i] != s2[i])
        {
            cnt++;
        }
    }
    
    return cnt == 1;
}

int solution(string begin, string target, vector<string> words) {
   
    queue<tuple<string, map<string, bool>, int>> q;
    
    map<string, bool> visited;
    for (string word : words)
    {
        visited[word] = false;
    }
    
    q.push({begin, visited, 0});
    
    while (!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        
        string word = get<0>(tmp);
        auto v = get<1>(tmp);
        int cnt = get<2>(tmp);
        
        if (word == target)
        {
            return cnt;
        }
        
        for (string w : words)
        {
            if (CheckString(word, w))
            {
                if (!v[w])
                {
                    v[w] = true;
                    q.push({w, v, cnt + 1});
                }
            }
        }
    }
    
    return 0;
}