#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> v1, vector<int> v2)
{
    return v1[1] < v2[1];
}

int solution(vector<vector<int>> routes) {
    int answer = 0;
    
    sort(routes.begin(), routes.end(), cmp);
    
    int cam_pos = -300001;
    for (vector<int> route : routes)
    {
        int s = route[0];
        int e = route[1];
        
        if (cam_pos < s)
        {
            cam_pos = e;
            answer++;
        }
    }  
    
    return answer;
}