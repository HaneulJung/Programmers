#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parent;

int getParent(int x)
{
    if (parent[x] == x) return x;
    return getParent(parent[x]);
}

void unionParent(int n1, int n2) 
{
    int a = getParent(n1);
    int b = getParent(n2);
    if (a > b) parent[a] = b;
    else parent[b] = a;
}

bool cmp(vector<int> a, vector<int> b)
{
    return a[2] < b[2];
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;    
    
    for (int i = 0; i < n; i++)
    {
        parent.push_back(i);
    }
    
    sort(costs.begin(), costs.end(), cmp);
    
    for (auto cost : costs)
    {
        if (getParent(cost[0]) != getParent(cost[1]))
        {
            answer += cost[2];
            unionParent(cost[0], cost[1]);
        }
    }
    
    return answer;
}