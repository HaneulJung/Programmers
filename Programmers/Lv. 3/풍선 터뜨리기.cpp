#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a) {
    int answer = 0;
    
    int size = a.size();
    
    vector<int> left(size, 0);
    vector<int> right(size, 0);
    
    int m = a[0];
    for (int i = 0; i < size; i++)
    {
        if (a[i] < m)
        {
            m = a[i];            
        }
        left[i] = m;
    }
    
    m = a[size-1];
    for (int i = size-1; i >= 0; i--)
    {
        if (a[i] < m)
        {
            m = a[i];            
        }
        right[i] = m;
    }
    
    for (int i = 0; i < size; i++)
    {
        bool isSmall_L = (left[i] < a[i]);
        bool isSmall_R = (right[i] < a[i]);
        
        if (isSmall_L && isSmall_R) continue;
        
        answer++;
    }
    
    return answer;
}