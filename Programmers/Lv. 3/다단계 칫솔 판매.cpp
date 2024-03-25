#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<string, string> parents;
unordered_map<string, int> profits;

void GetProfit(string child, int profit)
{    
    if (profit == 0)
    {
        return;
    }
    
    int p = int(profit * 0.1);
    
    profits[child] += (profit - p);
    if (parents[child] == "-")
    {
        return;
    }
    GetProfit(parents[child], p);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;
    
    for (int i = 0; i < enroll.size(); i++)
    {
        parents[enroll[i]] = referral[i];
        profits[enroll[i]] = 0;
    }
    
    for (int i = 0; i < seller.size(); i++)
    {
        GetProfit(seller[i], amount[i]*100);
    }
    
    for (string e : enroll)
    {
        answer.push_back(profits[e]);
    }
    
    return answer;
}