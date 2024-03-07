#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    queue<vector<int>> jobs_q;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> jobs_pq;
    
    sort(jobs.begin(), jobs.end());
    for (auto job : jobs)
    {
        jobs_q.push(job);
    }
    
    int start = -1;
    int now = 0;
    int idx = 0;
    while (idx < jobs.size())
    {
        while (!jobs_q.empty())
        {
            if (start < jobs_q.front()[0] && jobs_q.front()[0] <= now)
            {
                jobs_pq.push({jobs_q.front()[1], jobs_q.front()[0]});
                jobs_q.pop();
            }
            else
            {
                break;
            }
        }

        if (!jobs_pq.empty())
        {
            int work_time = jobs_pq.top().first;
            int request_time = jobs_pq.top().second;            
            jobs_pq.pop();

            start = now;
            now += work_time;
            answer += (now - request_time);
            idx++;
        }
        else
        {
            now++;
        }
    }
    
    
    return int(answer / jobs.size());
}