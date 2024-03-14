#include <vector>
#include <string>
#include <cstring>

using namespace std;

int solution(vector<string> arr)
{    
    int dp_max[101][101];
    int dp_min[101][101];
    
    memset(dp_max, -102000, sizeof(dp_max));
    memset(dp_min, 102000, sizeof(dp_min));
    
    vector<int> nums;
    vector<string> ops;
    for (int i = 0; i < arr.size(); i++)
    {
        if ((i % 2) == 0)
        {
            nums.push_back(stoi(arr[i]));
        }
        else
        {
            ops.push_back(arr[i]);
        }
    }
    
    for (int i = 0; i < nums.size(); i++)
    {
        dp_max[i][i] = nums[i];
        dp_min[i][i] = nums[i];
    }
    
    for (int d = 1; d < nums.size(); d++)
    {
        for (int s = 0; s < nums.size() - d; s++)
        {
            int e = s + d;
            for (int m = s; m < e; m++)
            {
                if (ops[m] == "+")
                {
                    dp_max[s][e] = max(dp_max[s][e], dp_max[s][m] + dp_max[m+1][e]);
                    dp_min[s][e] = min(dp_min[s][e], dp_min[s][m] + dp_min[m+1][e]);
                }  
                else
                {
                    dp_max[s][e] = max(dp_max[s][e], dp_max[s][m] - dp_min[m+1][e]);
                    dp_min[s][e] = min(dp_min[s][e], dp_min[s][m] - dp_max[m+1][e]);                  
                }    
            }
        }
    }
    
    return dp_max[0][nums.size()-1];
}