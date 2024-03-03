#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>

using namespace std;

vector<string> Split(string input, char dlim)
{
    vector<string> result;
    
    stringstream ss;
    string stringBuffer;
    ss.str(input);
    
    while (getline(ss, stringBuffer, dlim))
    {
        result.push_back(stringBuffer);
    }

	return result;
}

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    deque<int> dq;
    
    for (string op : operations)
    {
        auto tmp = Split(op, ' ');
        
        // Insert
        if (tmp[0] == "I")
        {
            dq.push_back(stoi(tmp[1]));
            
            // 오름차순 정렬
            sort(dq.begin(), dq.end());
        }
        // Delete
        else
        {     
            if (!dq.empty())
            {
                // Delete Max
                if (tmp[1] == "1")
                {
                    dq.pop_back();
                }
                // Delete Min
                else
                {
                    dq.pop_front();
                }
            }            
        }
    }
    
    if (dq.empty())
    {
        return {0, 0};
    }
    else
    {
        return {dq.back(), dq.front()};        
    }
}