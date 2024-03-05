#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

bool isPrime(int num)
{
    if ( num<=1 )
    {
        return false;
    }
    else
    {
        for (int i = 2; i < int(sqrt(double(num))) + 1; i++)
            if ( num % i == 0)
            {
                return false;
            }
    }
    
    return true;
}

set<int> nums;

void permutation(string str, bool *visited, string cur_str, int depth)
{
    if (depth > 0)
    {
        nums.insert(stoi(cur_str));
    }
    
    for (int i = 0; i < str.length(); i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            string new_str = cur_str + str[i];
            
            permutation(str, visited, new_str, depth+1);
            
            visited[i] = false;
        }
    }
}

int solution(string numbers) {
    bool visited[7] = {false, };
    
    permutation(numbers, visited, "", 0);
    
    int answer = 0;
    for (int s : nums)
    {
        if (isPrime(s))
        {
            answer++;
        }
    }
    return answer;
}