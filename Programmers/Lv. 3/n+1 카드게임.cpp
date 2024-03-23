#include <string>
#include <vector>

using namespace std;

int solution(int coin, vector<int> cards) {
    int answer = 0;
    
    int n = cards.size();
    
    vector<pair<int, int>> match;
    
    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (cards[i] + cards[j] == n + 1)
            {
                cards[i] = -10;
                cards[j] = -10;
                match.push_back({i, j});
            }
        }
    }
    
    int idx = n / 3 + 2;
    
    while (coin >= 0 && idx <= n)
    {        
        answer++;
        bool isPass = false;
        for (int i = 0; i < match.size(); i++)
        {
            auto p = match[i];
            if (p.first < idx && p.second < idx)
            {
                if (p.first >= n / 3 && p.second >= n / 3 && coin >= 2)
                {
                    isPass = true;
                    match[i] = {n, n};
                    coin -= 2;
                    break;
                }                
                else if (p.first < n / 3 && p.second >= n / 3  && coin >= 1)
                {
                    isPass = true;
                    match[i] = {n, n};
                    coin -= 1;
                    break;
                }                
                else if (p.first < n / 3 && p.second < n / 3)
                {
                    isPass = true;
                    match[i] = {n, n};
                    break;
                }
            }
        }
        if (!isPass)
        {
            break;
        }
        else
        {
            if (idx == n)
            {
                answer++;
            }
        }
        idx += 2;
    }
    
    return answer;
}