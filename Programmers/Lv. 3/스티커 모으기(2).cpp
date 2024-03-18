#include <iostream>
#include <vector>
using namespace std;

int solution(vector<int> sticker)
{
    int n = sticker.size();

    if (n == 1)
    {
        return sticker[0];
    }
    else if (n == 2)
    {
        return max(sticker[0], sticker[1]);
    }
    
    vector<int> dp1(n);
    vector<int> dp2(n);
    
    dp1[0] = sticker[0];
    dp1[1] = max(sticker[0], sticker[1]);    
    for (int i = 2; i < n - 1; i++)    
    {
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1]);
    }
    
    dp2[0] = 0;
    dp2[1] = sticker[1];    
    for (int i = 2; i < n; i++)    
    {
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1]);
    }

    return max(dp1[n-2], dp2[n-1]);
}