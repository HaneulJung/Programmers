#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> person1 = {1, 2, 3, 4, 5};
    vector<int> person2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    vector<int> results = {0, 0, 0};
    
    for (int i = 0; i < answers.size(); i++)
    {
        if (person1[i%5] == answers[i])
        {
            results[0]++;
        }
        if (person2[i%8] == answers[i])
        {
            results[1]++;
        }
        if (person3[i%10] == answers[i])
        {
            results[2]++;
        }
    }
    
    int max = *max_element(results.begin(), results.end());
    
    for (int i = 0; i < 3; i++)
    {
        if (max == results[i])    
        {
            answer.push_back(i+1);
        }
    }
    
    return answer;
}