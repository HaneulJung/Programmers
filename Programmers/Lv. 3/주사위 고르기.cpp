#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<vector<int>> dice;
vector<vector<int>> combs1;
vector<vector<int>> combs2;
map<vector<int>, int> wins;

void combination(int size, vector<bool> visited, vector<int> cur_v, int depth, int r)
{
    if (depth == r)
    {
        combs1.push_back(cur_v);
        
        vector<int> tmp;
        for (int j = 0; j < size; j++)
        {
            if (count(cur_v.begin(), cur_v.end(), j) == 0)
            {
                tmp.push_back(j);
            }            
        }
        combs2.push_back(tmp);
    }
    
    for (int i = 0; i < size; i++)
    {
        if (visited[i]) continue;
        
        visited[i] = true;
        
        vector<int> new_v(cur_v);
        new_v.push_back(i);
        combination(size, visited, new_v, depth+1, r);
    }
}

void GetSum(vector<int>& sum_v, vector<int> comb, int cur_s, int depth)
{
    if (depth == comb.size())
    {
        sum_v.push_back(cur_s);
        return;
    }
    
    for (int i = 0; i < 6; i++)
    {
        GetSum(sum_v, comb, cur_s + dice[comb[depth]][i], depth+1);
    }
}

int CountWin(vector<int> a, vector<int> b)
{
    int total = 0;
    for(int i = 0; i < a.size(); i++)
    {
        int begin = 0;
        int end = b.size() - 1;

        while (begin <= end)
        {
            int mid = (begin + end) / 2;
            
            if(a[i] > b[mid])
            {
                begin = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }
        total += begin;
    }
    return total;
}

bool cmp(pair<vector<int>, int> a, pair<vector<int>, int> b)
{
    return a.second > b.second;
}

vector<int> solution(vector<vector<int>> dice_) {
    dice = dice_;
    
    int size = dice.size();
    vector<bool> visited(size);
    vector<int> tmp_v;
    
    combination(size, visited, tmp_v, 0, size / 2);
    
    for (int i = 0; i < combs1.size(); i++)
    {
        vector<int> sum_v1;
        GetSum(sum_v1, combs1[i], 0, 0);
        vector<int> sum_v2;
        GetSum(sum_v2, combs2[i], 0, 0);

        sort(sum_v1.begin(), sum_v1.end());
        sort(sum_v2.begin(), sum_v2.end());

        int cnt = CountWin(sum_v1, sum_v2);

        wins[combs1[i]] = cnt;  
    }
    
    vector<pair<vector<int>, int>> vec( wins.begin(), wins.end() );

    sort(vec.begin(), vec.end(), cmp);       
    
    vector<int> answer;
    for (int n : vec[0].first)
    {
        answer.push_back(n+1);
    }
        
    return answer;
}