#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer = {};
    int pre = -1;
    
    for (int a : arr)
    {
        if (a != pre)
        {
            answer.push_back(a);
            
            pre = a;
        }
    }

    return answer;
}