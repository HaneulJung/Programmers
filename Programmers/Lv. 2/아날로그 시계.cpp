#include <string>
#include <vector>

using namespace std;

vector<double> getAngles(int seconds)
{
    /*
        1초에 움직이는 각도
        시침 - 1/120도
        분침 - 1/10도
        초침 - 6도
    */
    
    int h = seconds / 3600;
    int m = (seconds % 3600) / 60;
    int s = (seconds % 3600) % 60;
    
    double hDegree = (h % 12) * 30.0 + m * 0.5 + s * (1/120.0);
    double mDegree = m * 6.0 + s * (0.1);
    double sDegree = s * 6.0;
    
    return {hDegree, mDegree, sDegree};
}

bool CheckMatch(double a1, double b1, double a2, double b2)
{
    if (a1 > b1 && a2 <= b2)
    {
        return true;
    }
    
    if (b2 == 0 && a1 > 354)
    {
        return true;           
    }
    
    return false;
}

int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    int answer = 0;
    
    int startTime = s1 + m1 * 60 + h1 * 3600;
    int endTime = s2 + m2 * 60 + h2 * 3600;
        
    vector<double> curAngles, preAngles;
    curAngles = getAngles(startTime);
    
    if (curAngles[0] == curAngles[2] || curAngles[1] == curAngles[2])
    {
        answer++;
    }
    
    for (int t = startTime+1; t < endTime+1; t++)
    {        
        curAngles = getAngles(t);
        preAngles = getAngles(t-1);
        
        bool hourMatch = CheckMatch(preAngles[0], preAngles[2], curAngles[0], curAngles[2]);
        bool minuteMatch = CheckMatch(preAngles[1], preAngles[2], curAngles[1], curAngles[2]);
        
        if (hourMatch && minuteMatch)
        {
            if (curAngles[0] == curAngles[1])
            {
                answer++;
            }
            else
            {
                answer += 2;
            }
        }
        else if (hourMatch || minuteMatch)
        {
            answer++;
        }
    }    
    
    return answer;
}