#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    vector<vector<int>> results;
    results.push_back({triangle[0]});
    
    for (int i = 1; i < triangle.size(); i++)
    {
        vector<int> tmp_v;
        for (int j = 0; j < triangle[i].size(); j++)
        {
            int tmp_l = 0;
            int tmp_r = 0;
            
            if (j >= 1)
            {
                tmp_l = triangle[i][j] + results[i-1][j-1];
            }
            if (j < triangle[i].size() - 1)
            {
                tmp_r = triangle[i][j] + results[i-1][j];
                
            }
            
            int m = max({tmp_l, tmp_r});
            
            tmp_v.push_back(m);
        }
        results.push_back(tmp_v);
    }
    
    auto r = results[results.size()-1];
    
    return *max_element(r.begin(), r.end());
}