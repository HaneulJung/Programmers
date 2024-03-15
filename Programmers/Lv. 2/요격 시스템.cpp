#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b)
{
    return a[1] < b[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 0;
    
    sort(targets.begin(), targets.end(), cmp);
    
    int missile = 0;
    for (vector<int> target : targets)
    {
        int s = target[0];
        int e = target[1];
        
        if (missile <= s)
        {
            missile = e;
            answer++;
        }
    }   
        
    return answer;
}