#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> stones, int k) {
    int answer = 0;
    
    int start = *min_element(stones.begin(), stones.end());
    int end = *max_element(stones.begin(), stones.end());
    
    while (start <= end)
    {
        int mid = (start + end) / 2;
        
        int max_cnt = 0;
        int cnt = 0;
        for (int stone : stones)
        {
            int tmp = stone - mid;
            
            if (tmp < 0)
            {
                cnt++;
            }
            else
            {
                cnt = 0;
            }
            max_cnt = max(max_cnt, cnt);
        }
        
        if (max_cnt >= k)
        {
            end = mid - 1;
        }
        else
        {
            answer = mid;
            start = mid + 1;
        }
    }
    
    return answer;
}