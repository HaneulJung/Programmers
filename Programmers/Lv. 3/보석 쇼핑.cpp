#include <string>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    
    set<string> s;
    
    for (string gem : gems)
    {
        s.insert(gem);
    }
    
    int n = s.size();
    
    unordered_map<string, int> um;
    
    int begin = 1;
    int end = 1;
    
    um[gems[0]] = 1;
    int cnt = 1;
        
    int min_length = gems.size();
    
    while (end <= gems.size())
    {
        if (cnt < n)
        {
            end++;
            
            if (end > gems.size())
            {
                break;
            }
            
            if (um[gems[end-1]] == 0)
            {
                cnt++;
            }
            
            um[gems[end-1]]++;
        }
        else
        {
            if (end - begin < min_length)   
            {
                min_length = end - begin;
                answer = {begin, end};
            }
            
            if (um[gems[begin-1]] == 1)
            {
                cnt--;
            }
            
            um[gems[begin-1]]--;
            
            begin++;
        }        
    }    
    
    return answer;
}