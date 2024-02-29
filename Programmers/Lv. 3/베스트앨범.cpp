/*
장르를 나타내는 문자열 배열 genres
노래별 재생 횟수를 나타내는 정수 배열 plays
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
*/

#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool compareByValue(pair<string, int>& a, pair<string, int>& b) {
    return a.second > b.second;
}

bool compareByPlay(pair<int, int>& a, pair<int, int>& b) {
    if (a.second == b.second)
    {
        return a.first < b.first;
    }
    return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    map<string, int> cnt_by_genres;
    map<string, vector<pair<int, int>>> idx_type;
    
    for (int i = 0; i < genres.size(); i++)
    {
        if (cnt_by_genres.count(genres[i]) == 0)
        {
            cnt_by_genres[genres[i]] = 0;
            idx_type[genres[i]] = {};
        }
        cnt_by_genres[genres[i]] += plays[i];
        idx_type[genres[i]].push_back({i, plays[i]});
    }
    
    vector<pair<string,int>> v_cnt_by_genres(cnt_by_genres.begin(), cnt_by_genres.end());
    
    sort(v_cnt_by_genres.begin(), v_cnt_by_genres.end(), compareByValue);
    for (auto pair : v_cnt_by_genres)
    {
        auto tmp = idx_type[pair.first];
        sort(tmp.begin(), tmp.end(), compareByPlay);
        answer.push_back(tmp[0].first);
        if (tmp.size() > 1)
        {
            answer.push_back(tmp[1].first);
        }
    } 
    
    return answer;
}