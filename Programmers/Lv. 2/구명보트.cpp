#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    deque<int> dq;
    
    sort(people.begin(), people.end());
    
    for (int p : people)
    {
        dq.push_back(p);
    }
    
    while (!dq.empty())
    {
        int min = dq.front();
        int max = dq.back();
        
        if ((min + max) <= limit)
        {
            dq.pop_front();
        }
        
        if (!dq.empty())
        {
            dq.pop_back();    
        }        
        
        answer++;
    }
    
    return answer;
}


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(), people.end());
    
    int s = 0;
    int e = people.size() - 1;
    
    while (s <= e)
    {
        if ((people[s] + people[e]) <= limit)
        {
            s++;
        }
        e--;
        answer++;
    }    
    
    return answer;
}