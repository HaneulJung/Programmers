#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string, int> clothes_map;
    for (vector<string> clothe : clothes)
    {        
        string type = clothe[1];
        
        if (clothes_map.count(type) == 0)
        {
            clothes_map[type] = 1;
        }
        clothes_map[type]++;
    }
    
    for (auto pair : clothes_map)
    {
        answer *= pair.second;
    }
    
    return answer - 1;
}