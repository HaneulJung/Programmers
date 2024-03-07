#include <string>
#include <vector>
#include <map>

using namespace std;

map<char, int> alpha = {
    {'A', 0}, {'E', 1}, {'I', 2}, {'O', 3}, {'U', 4}
};

int solution(string word) {
    int answer = 0;
    
    int tmp[] = {781, 156, 31, 6, 1};
    
    int idx = 0;
    for (char w : word)
    {
        answer += tmp[idx] * alpha[w];
        idx++;
    }
    
    return answer + word.length();
}