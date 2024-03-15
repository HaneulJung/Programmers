#include <string>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

bool cmp(vector<int> a, vector<int> b)
{
    for (int i = 10; i > -1; i--)
    {
        if (a[i] > b[i]){
            return true;
        }
        else if (a[i] < b[i])
        {
            return false;
        }
    }
    return false;
}

vector<int> solution(int n, vector<int> info) {
    vector<int> answer(11);
    
    queue<tuple<int, int, int, vector<int>>> q;
    vector<int> v;
    q.push({0, 0, n, v}); // 현재 위치, 현재 점수, 남은 화살 개수, 점수 배열
    
    int max_score = 0;
    
    while (!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        int pos = get<0>(tmp);
        int score = get<1>(tmp);
        int arrow = get<2>(tmp);
        vector<int> tmp_v = get<3>(tmp);
        
        if (pos == 10)
        {
            tmp_v.push_back(arrow);
            
            if (score > max_score)
            {                
                max_score = score;
                answer = tmp_v;  
            }
            else if (score == max_score)
            {
                if (cmp(tmp_v, answer))
                {
                    answer = tmp_v;     
                } 
            }
        }
        else
        {
            int cur_score = 10 - pos;
            
            
            // 지는 거
            if (info[pos] > 0)
            {
                tmp_v.push_back(0);
                q.push({pos+1, score - cur_score, arrow, tmp_v});    
            }
            // 비기는 거
            else
            {
                tmp_v.push_back(0);
                q.push({pos+1, score, arrow, tmp_v});   
            }      
            
            if (arrow > info[pos])
            {
                // 이기는 거
                tmp_v = get<3>(tmp);
                tmp_v.push_back(info[pos]+1);
                q.push({pos+1, score + cur_score, arrow - (info[pos]+1), tmp_v});
            }
        }       
    }
    
    if (max_score == 0)
    {
        return {-1};    
    }
    return answer;
}