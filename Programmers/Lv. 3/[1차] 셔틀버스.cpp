#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <queue>

using namespace std;

int GetMinutes(string time)
{
    stringstream ss(time);
    string s;
    
    vector<string> t;
    
    while (getline(ss, s, ':'))
    {
        t.push_back(s);
    }
           
    return stoi(t[0])*60 + stoi(t[1]);
}

string MinuteToString(int time)
{
    int h = time / 60;
    int m = time % 60;
    
    string result = "";
    if (h <10)
    {
        result += "0";
    }
    result += to_string(h);
    result += ":";
    
    if (m<10)
    {
        result += "0";
    }
    result += to_string(m);
    
    return result;
}

string solution(int n, int t, int m, vector<string> timetable) {
       
    vector<int> waiting;
    for (string time : timetable)
    {
        waiting.push_back(GetMinutes(time));
    }    
    sort(waiting.begin(), waiting.end());
    
    queue<int> people;
    for (int w : waiting)
    {
        people.push(w);
    }
    
    vector<int> shuttleTimes;
    vector<pair<int, vector<int>>> shuttles;
    
    int firstBus = GetMinutes("09:00");
    for (int i = 0; i < n; i++)
    {
        shuttleTimes.push_back(firstBus + i * t);
    }
    
    for (int shuttleTime : shuttleTimes)
    {        
        vector<int> tmp;
        while (!people.empty())
        {
            if (tmp.size() >= m)
            {
                break;
            }
            
            int curPeople = people.front();
            if (curPeople <= shuttleTime)
            {
                tmp.push_back(curPeople);
                people.pop();
            }
            else
            {
                break;
            }
        }
        shuttles.push_back({shuttleTime, tmp});
    }
    
    if (shuttles[n-1].second.size() < m)
    {
        return MinuteToString(shuttles[n-1].first);
    }
    else
    {
        return MinuteToString(shuttles[n-1].second[m-1]-1);   
    }
}