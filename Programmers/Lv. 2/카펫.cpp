#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    
    for (int i = 1; i <= int(yellow / 2); i++)
    {
        if ((yellow % i) == 0)
        {
            int w = int(yellow / i);
            int h = i;
            
            if ((int((w + 2) * (h + 2)) - yellow) == brown)
            {
                return {w+2, h+2};
            }
        }
    }
    
    return {3, 3};
}