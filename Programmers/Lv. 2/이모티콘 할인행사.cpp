#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int rates[4] = {10, 20, 30, 40};

vector<vector<int>> sale_rates;

void dfs(vector<int> v, int depth)
{
    if (v.size() == depth)
    {
        sale_rates.push_back(v);
        return;
    }
    for (int rate : rates)
    {
        v.push_back(rate);
        dfs(v, depth);
        v.pop_back();
    }
}

bool cmp(vector<int> a, vector<int> b)
{
    if (a[0] == b[0])
    {
        return a[1] > b[1];
    }
    
    return a[0] > b[0];
}

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    int emo_num = emoticons.size();
    
    vector<int> v;
    dfs(v, emo_num);
    
    
    vector<vector<int>> results;
    
    for (vector<int> sr : sale_rates)
    {
        int plus_num = 0;
        int price_sum = 0;
        
        for (auto user : users)
        {
            int tmp_sum = 0;
            for (int i = 0; i < emo_num; i++)
            {
                if (sr[i] >= user[0])
                {
                    tmp_sum += (emoticons[i] * (100 - sr[i]) / 100);
                }
            }
            if (tmp_sum >= user[1])
            {
                plus_num++;
            }
            else
            {
                price_sum += tmp_sum;    
            }
        }   
        results.push_back({plus_num, price_sum});
    }
    
    sort(results.begin(), results.end(), cmp);
    
    return results[0];
}