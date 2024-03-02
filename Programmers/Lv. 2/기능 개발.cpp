#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    queue<int> elapsedDays = {};
    
    for (int i = 0; i < speeds.size(); i++)
    {
        if ((100 - progresses[i]) % speeds[i] == 0)
        {
            elapsedDays.push((100 - progresses[i]) / speeds[i]);
        }
        else
        {
            elapsedDays.push(((100 - progresses[i]) / speeds[i]) + 1);
        }
    }
                
    while (!elapsedDays.empty())
    {
        int cnt = 1;
        int cur = elapsedDays.front();
        elapsedDays.pop();

        while(cur >= elapsedDays.front() && !elapsedDays.empty()) {
            elapsedDays.pop();
            cnt++;
        }

        answer.push_back(cnt);
    }
        
    return answer;
}