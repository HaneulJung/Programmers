#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    
    vector<char> tmp = {number[0]};
    
    for (int i = 1; i < number.length(); i++)
    {
        while (k > 0 && int(tmp.back()) < int(number[i]) && tmp.size() > 0)
        {
            tmp.pop_back();
            k--;
        }
        tmp.push_back(number[i]);
    }
    
    for (int i = 0; i < tmp.size() - k; i++)
    {
        answer += tmp[i];
    }
    return answer;
}