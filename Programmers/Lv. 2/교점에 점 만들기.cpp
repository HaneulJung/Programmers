#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;

vector<string> solution(vector<vector<int>> line) {
    vector<string> answer;
    set<pair<ll, ll>> stars;
    
    for (int i = 0; i < line.size(); i++)
    {
        for (int j = 0; j < line.size(); j++)    
        {
            if (i == j) continue;
            
            ll e1 = ll(line[i][1]) * ll(line[j][2]) - ll(line[i][2]) * ll(line[j][1]);
            ll e2 = ll(line[i][2]) * ll(line[j][0]) - ll(line[i][0]) * ll(line[j][2]);
            ll e3 = ll(line[i][0]) * ll(line[j][1]) - ll(line[i][1]) * ll(line[j][0]);
                        
            if (e3 != 0 && (e1 % e3 == 0) && (e2 % e3 == 0))
            {
                stars.insert({e1 / e3, e2 / e3});
            }
        }
    }
    
    ll max_x = -9223372036854775807, min_x = 9223372036854775807, 
        max_y = -9223372036854775807, min_y = 9223372036854775807;
    for (auto p : stars)
    {
        if (p.first > max_x) max_x = p.first;
        if (p.first < min_x) min_x = p.first;
        if (p.second > max_y) max_y = p.second;
        if (p.second < min_y) min_y = p.second;
    }
    
    for (ll y = max_y; y > min_y - 1; y--)
    {
        string tmp;
        for (ll x = min_x; x < max_x + 1; x++)
        {
            if (count(stars.begin(), stars.end(), make_pair(x, y)) != 0)
            {
                tmp += '*';
            }
            else
            {
                tmp += '.';
            }
        }
        answer.push_back(tmp);
    }
    
    return answer;
}