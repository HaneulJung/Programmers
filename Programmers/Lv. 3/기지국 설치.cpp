#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer = 0;
    
    int cur = 1;
    stations.push_back(n+w+1);
    for (int station : stations)
    {
        int start = station - w;
        int end = station + w;
        
        if (start > cur)
        {
            answer += (start - cur - 1) / (2*w+1) + 1;
        }
        cur = end + 1;
    }
    
    return answer;
}