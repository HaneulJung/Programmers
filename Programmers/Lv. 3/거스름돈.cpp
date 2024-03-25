#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> money) {
    sort(money.begin(), money.end());
    vector<int> dp(n+1, 0);
    dp[0] = 1;
    
    for (int m : money)
    {
        for (int i = m; i < n + 1; i++)
        {
            dp[i] += dp[i-m];
            dp[i] %= 1000000007;
        }
    }
    
    return dp[n];
}