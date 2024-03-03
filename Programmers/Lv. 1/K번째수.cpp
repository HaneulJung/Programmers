#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (int i = 0; i < commands.size(); i++)
    {
        int s = commands[i][0];
        int e = commands[i][1];
        int pos = commands[i][2];
        
        vector<int> tmp;
        for (int j = s-1; j < e; j++)
        {
            tmp.push_back(array[j]);
        }
        
        sort(tmp.begin(), tmp.end());
        
        answer.push_back(tmp[pos-1]);
    }
    
    return answer;
}