#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int longer = 0, shorter = 0;
    
    for (vector<int> size : sizes)
    {
        int max = *max_element(size.begin(), size.end());
        int min = *min_element(size.begin(), size.end());
        
        if (max > longer)
        {
            longer = max;
        }
        
        if (min > shorter)
        {
            shorter = min;
        }
    }
    
    return longer * shorter;
}