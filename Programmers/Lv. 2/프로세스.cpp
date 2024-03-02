#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> q;
    
    for (int i = 0; i < priorities.size(); i++)
    {
        q.push({priorities[i], i});
    }
    
    int cnt = 1;
    while (true)
    {
        int max = *max_element(priorities.begin(), priorities.end());
        
        int value = q.front().first;        
        int loc = q.front().second;        
        q.pop();
        
        if (value == max)
        {
            if (loc == location)
            {
                return cnt;
            }
            priorities[loc] = 0;
            cnt++;
        }
        else
        {
            q.push({value, loc});
        }
    }
}