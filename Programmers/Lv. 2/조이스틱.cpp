#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<char, int> alphabet = {
    {'A', 0}, {'B', 1}, {'C', 2}, {'D', 3}, {'E', 4}, {'F', 5}, {'G', 6}, {'H', 7},
    {'I', 8}, {'J', 9}, {'K', 10}, {'L', 11}, {'M', 12}, {'N', 13}, {'O', 12}, {'P', 11},
    {'Q', 10}, {'R', 9}, {'S', 8}, {'T', 7}, {'U', 6}, {'V', 5}, {'W', 4}, {'X', 3},
    {'Y', 2}, {'Z', 1}
};

int solution(string name) {
    int answer = alphabet[name[0]];
    
    vector<pair<int, int>> v;
    int pos = 0;
    int c = 0;
    for (int i = 1; i < name.length(); i++)
    {
        answer += alphabet[name[i]];
        
        if (name[i] == 'A')
        {            
            if (c == 0)
            {
                pos = i;
            }
            c++;
            
            if (i == name.length() - 1)
            {
                v.push_back({pos, c});
            }
        }
        else
        {
            if (c != 0)
            {
                v.push_back({pos, c});
                c = 0;
            }
        }
    }

    int l = name.length();
    
    vector<int> mins = {l-1};
    
    for (auto pair : v)
    {
        
        int a = pair.first;
        int b = pair.second;
        
        int min1 = (a-1)*2 + l - (a + b);
        int min2 = (l-(a+b))*2 + a - 1;
        
        mins.push_back(min1);
        mins.push_back(min2);
    }
    
    int m = *min_element(mins.begin(), mins.end());
    
    return answer + m;
}