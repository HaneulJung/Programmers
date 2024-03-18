#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int idx_A = 0;
    for (int b : B)
    {
        if (b > A[idx_A])
        {
            answer++;
            idx_A++;
        }
    }
    
    
    return answer;
}