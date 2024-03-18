#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    
    priority_queue<int> pq;
    
    int sum = 0;
    for (int work : works)
    {
        pq.push(work);
        
        sum += work;
    }
        
    if (n >= sum)
    {
        return 0;        
    }
    
    while (n > 0)
    {
        int value = pq.top();
        pq.pop();
        pq.push(value-1);
        n--;
    }
    
    while (!pq.empty())
    {
        int num = pq.top();
        pq.pop();
        answer += num*num; 
    }
    
    return answer;
}