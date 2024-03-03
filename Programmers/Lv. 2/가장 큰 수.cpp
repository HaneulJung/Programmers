#include <string>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(int a, int b)
{
    string s_a = to_string(a);
    string s_b = to_string(b);
    
    string tmp_a, tmp_b;
    for (int i = 0; i < 4; i++)
    {
        tmp_a += s_a;
        tmp_b += s_b;
    }
    
    return stoi(tmp_a.substr(0, 4)) > stoi(tmp_b.substr(0, 4));
}

string solution(vector<int> numbers) {
    string answer = "";
    
    sort(numbers.begin(), numbers.end(), cmp);
    
    for (int number : numbers)
    {
        answer += to_string(number);
    }
    
    if (answer[0] == '0')
    {
        return "0";
    }
    
    return answer;
}