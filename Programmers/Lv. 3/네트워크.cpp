#include <string>
#include <vector>
#include <set>

using namespace std;
    
vector<int> parents;

int getParent(int n)
{
    if (parents[n] == n)
    {
        return n;
    }
    return getParent(parents[n]);
}

void unionParent(int n1, int n2)
{
    int a = getParent(n1);
    int b = getParent(n2);
    
    if (a < b)
    {
        parents[b] = a;
    }
    else
    {
        parents[a] = b;
    }
}

int solution(int n, vector<vector<int>> computers) {    
    for (int i = 0; i < n; i++)
    {
        parents.push_back(i);
    }
    
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (computers[i][j] == 1)
            {
                unionParent(i, j);
            }
        }
    }
    
    set<int> s;
    for (int p : parents)
    {
        s.insert(getParent(p));
    }
    return s.size();
}