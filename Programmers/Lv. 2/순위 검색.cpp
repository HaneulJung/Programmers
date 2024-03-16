#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <algorithm>

using namespace std;

unordered_map<string, vector<int>> um;
vector<vector<string>> tmp(4, vector<string>(2, "-"));

void Split_Info(string input)
{        
    stringstream ss;
    string stringBuffer;
    ss.str(input);
    
    int pos = 0, score = 0;
    while (ss >> stringBuffer)
    {
        if (pos == 4)
        {
            score = stoi(stringBuffer);
        }
        else
        {
            tmp[pos][0] = stringBuffer;
            pos++;    
        }        
    }    
    
    string s1, s2, s3, s4;
    for (int i = 0; i < 2; i++)
    {
        s1 = tmp[0][i];
        for (int j = 0; j < 2; j++)    
        {
            s2 = tmp[1][j];
            for (int k = 0; k < 2; k++)
            {
                s3 = tmp[2][k];
                for (int p = 0; p < 2; p++)
                {
                    s4 = tmp[3][p];
                    um[s1+s2+s3+s4].push_back(score);        
                }
            }
        }
    }
}

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    
    for (string in : info)
    {
        Split_Info(in);    
    }
    
    for (auto it : um)
    {
        sort(um[it.first].begin(), um[it.first].end());
    }
    
    for (string q: query) {
        string s, key = "";
        int idx = 0, score = 0;
        
        stringstream ss(q);
        
        while (ss >> s) {
            if (s == "and") continue;
            
            if (idx < 4) {
                key += s;
                idx++;
            } else {
                score = stoi(s);
            }
        }
        
        
        
        auto it = lower_bound(um[key].begin(), um[key].end(), score);
        answer.push_back(um[key].size() - (it - um[key].begin()));
    }
    
    return answer;
}