#include <string>
#include <vector>
#include <deque>

using namespace std;

int Sum(deque<int> dq)
{
    int s = 0;
    for (int t : dq) 
    {
        s += t;
    }
    return s;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    
    deque<int> q_waiting_trucks = {};
    deque<int> q_going_trucks = {};
    deque<int> q_positions = {};
    
    for (int tw : truck_weights)
    {
        q_waiting_trucks.push_back(tw);
    }
    
    while (!q_waiting_trucks.empty() || !q_going_trucks.empty())
    {
        for (int i = 0; i < q_positions.size(); i++)
        {
            q_positions[i]++;
        }
        
        if (q_positions[0] == bridge_length)
        {
            q_going_trucks.pop_front();
            q_positions.pop_front();
        }
       
        if (!q_waiting_trucks.empty())
        {
            if ((Sum(q_going_trucks) + q_waiting_trucks[0]) <= weight)
            {
                q_going_trucks.push_back(q_waiting_trucks.front());
                q_waiting_trucks.pop_front();
                q_positions.push_back(0);
            }
        }
        
        answer++;
    }
    
    return answer;
}