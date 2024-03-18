#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int ceil(double n)
{
    int tmp = int(n);
    if (double(tmp) == n)
    {
        return tmp;
    }
    else
    {
        return tmp + 1;
    }
}

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    while (n > 0)
    {
        int tmp = ceil(double(s) / double(n));
        
        s -= tmp;        
        answer.push_back(tmp);
        
        n--;
        
        if (s <= 0 && n > 0)
        {
            return {-1};
        }
    }
        
    sort(answer.begin(), answer.end());
    
    return answer;
}