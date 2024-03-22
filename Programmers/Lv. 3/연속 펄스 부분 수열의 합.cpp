#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(vector<int> sequence) {
    int size = sequence.size();
    
    vector<int> sequence1;  // 홀수 번째에 -1 곱하기
    vector<int> sequence2;  // 짝수 번째에 -1 곱하기
    
    for (int i = 0; i < size; i++)
    {
        if (i % 2 == 0)
        {
            sequence1.push_back(sequence[i]);
            sequence2.push_back(-sequence[i]);
        }
        else
        {
            sequence1.push_back(-sequence[i]);
            sequence2.push_back(sequence[i]);
        }
    }
    
    vector<long long> dp1(size);
    dp1[0] = sequence1[0];
    vector<long long> dp2(size);
    dp2[0] = sequence2[0];
    
    for (int i = 1; i < size; i++)
    {
       dp1[i] = max((long long)sequence1[i], dp1[i-1] + sequence1[i]);
       dp2[i] = max((long long)sequence2[i], dp2[i-1] + sequence2[i]);
    }
        
    return max(*max_element(dp1.begin(), dp1.end()), *max_element(dp2.begin(), dp2.end()));
}