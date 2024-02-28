#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(vector<int> nums)
{
    int N = nums.size();
    map<int, int> pocketmons;
    
    for (int num : nums)
    {
        if (pocketmons.count(num) == 0)
        {
            pocketmons[num] = 0;
        }
        pocketmons[num]++;
    }
        
    return min((int)(N/2), (int)(pocketmons.size()));
}