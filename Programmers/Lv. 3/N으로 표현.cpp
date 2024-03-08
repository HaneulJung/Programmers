#include <string>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int solution(int N, int number) {
    
    set<int> results[9];
    
    for (int i = 1; i < 9; i++)
    {
        // 1. 숫자 N이 그냥 옆에 더해지는 거 (ex. 5 -> 55)
        string tmp;
        for (int j = 1; j < i + 1; j++)
        {
            tmp += to_string(N);
        }
        results[i].insert(stoi(tmp));
        
        for (int j = 0; j < i; j++)
        {
            for (int s1 : results[j])
            {
                for (int s2 : results[i-j])
                {
                    // 2. 더하기 (ex. 5 + 5)
                    results[i].insert(s1 + s2);

                    // 3. 빼기 (ex. 5 - 5)
                    results[i].insert(s1 - s2);
                    results[i].insert(s2 - s1);

                    // 4. 곱하기 (ex. 5 * 5)
                    results[i].insert(s1 * s2);

                    // 5. 나누기 (ex. int(5 / 5)) // 나머지 무시
                    if (s1 != 0)
                    {
                        results[i].insert(int(s2 / s1));                        
                    }
                    if (s2 != 0)
                    {
                        results[i].insert(int(s1 / s2));                        
                    }
                }
            }
        }
        
        auto iter = find(results[i].begin(), results[i].end(), number);
        if (iter != results[i].end())
        {
            return i;
        }
    }
    
    return -1;
}