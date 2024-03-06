#include <string>
#include <vector>

using namespace std;

int answer = 0;
void makeExpression(vector<int> v, int cur_value, int depth, int r, int t)
{
    if (depth == r)
    {
        if (cur_value == t)
        {
            answer++;    
        }        
        return;
    }
    
    int new_value = cur_value + v[depth];
    makeExpression(v, new_value, depth + 1, r, t);

    new_value = cur_value - v[depth];
    makeExpression(v, new_value, depth + 1, r, t);
}
int solution(vector<int> numbers, int target) {
        
    makeExpression(numbers, 0, 0, numbers.size(), target);
    
    return answer;
}