#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long startTime = 1, 
        endTime = *max_element(times.begin(), times.end()) * n, 
        elapsedTime;
    long long people;
    
    while (true)
    {
        if (startTime == endTime)
        {
            return startTime;
        }
        
        elapsedTime = (startTime + endTime) / 2;
    
        people = 0;
        for (int time : times)
        {
            people += elapsedTime / time;
        }

        if (people >= n)
        {
            endTime = elapsedTime;
        }
        else
        {
            startTime = elapsedTime + 1;
        } 
    }
   
    return 0;
}