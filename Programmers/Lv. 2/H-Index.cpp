#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int max = *max_element(citations.begin(), citations.end());
    for (int i = max; i > 0; i--)
    {
        int cnt = 0;
        for (int c : citations)     
        {
            if (c >= i)
            {
                cnt++;
            }
        }
        if (cnt >= i)
        {
            return i;
        }
    }
}