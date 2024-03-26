#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b)
{
    return a[0]+a[1] > b[0]+b[1];
}

int solution(vector<vector<int>> scores) {
    int answer = 1;
    
    sort(scores.begin()+1, scores.end(), cmp);
    
    int whanho_sum = scores[0][0] + scores[0][1];
        
    for (int i = 1; i < scores.size(); i++)
    {
        if (scores[0][0] < scores[i][0] && scores[0][1] < scores[i][1])
        {
            return -1;                
        }
        
        if (whanho_sum < scores[i][0] + scores[i][1])
        {
            answer++;
        }       
        else
        {
            break;
        }
    }
    
    int rank = answer;
    for(int c = rank-1; c > 0; c--)
    {
        for(int p = c - 1; p >= 0; p--)
        {        
            if(scores[c][0] < scores[p][0] 
               && scores[c][1] < scores[p][1])
            {
                answer--;
                break;
            }
        }
    }
    
    return answer;
}