#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {       
    int answer = 0;
    
    sort(rocks.begin(), rocks.end());
    rocks.push_back(distance);
    
    int s = 0;
    int e = distance;
    
    while (s <= e)
    {
        int min_value = 1000000001;
        int m = (s + e) / 2;
        int cur_pos = 0;
        int cnt = 0;
        for (int rock : rocks)
        {
            if (rock - cur_pos < m)
            {
                cnt++;                
            }
            else
            {
                min_value = min(min_value, rock - cur_pos);
                
                cur_pos = rock;
                
            }
        }    
        
        if (cnt > n)
        {
            e = m - 1;
        }
        else
        {
            answer = min_value;
            s = m + 1;
        }
    }    
    
    return answer;
}