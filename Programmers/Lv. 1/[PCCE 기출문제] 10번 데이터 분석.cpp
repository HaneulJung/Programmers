/*
["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]

2차원 정수 리스트 data
어떤 정보 기준으로 데이터 뽑아낼지 의미하는 문자열 ext
뽑아낼 정보의 기준값을 나타내는 정수 val_ext,
정보를 정렬할 기준이 되는 문자열 sort_by

data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
*/

#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

map<string, int> extMap = {
        {"code", 0},
        {"date", 1},
        {"maximum", 2},
        {"remain", 3}
    };

int sortBy = 0;

bool cmp(vector<int> &v1, vector<int> &v2)        
{
    return v1[sortBy] < v2[sortBy];
}

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;

    sortBy = extMap[sort_by];    

    for (int i = 0; i < data.size(); i++)
    {
        if (data[i][extMap[ext]] < val_ext)
        {
            answer.push_back(data[i]);
        }
    }

    sort(answer.begin(), answer.end(), cmp);

    return answer;
}