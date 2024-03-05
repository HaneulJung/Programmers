#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    vector<int> new_lost(lost);
    
    for (int l : lost)
    {
        auto iter = find(reserve.begin(), reserve.end(), l);
        if (iter != reserve.end())
        {
            reserve.erase(iter);
            
            iter = find(new_lost.begin(), new_lost.end(), l);
            new_lost.erase(iter);
        }
    }
    
    sort(reserve.begin(), reserve.end());
    sort(new_lost.begin(), new_lost.end());
    
    for (int r : reserve)
    {
        auto tmp = find(new_lost.begin(), new_lost.end(), r-1);
        if (tmp != new_lost.end())
        {
            new_lost.erase(tmp);
            continue;
        }
        tmp = find(new_lost.begin(), new_lost.end(), r+1);
        if (tmp != new_lost.end())
        {
            new_lost.erase(tmp);
        }
    }  
    
    return n - new_lost.size();
}