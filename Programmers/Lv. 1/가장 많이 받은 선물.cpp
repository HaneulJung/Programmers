/*
두 사람이 선물을 주고받은 기록이 있으면 더 많이 준 사람이 다음 달에 선물 하나 받음
선물 주고받지 않았거나 주고받은 수가 같으면 선물 지수가 더 큰 사람이 선물 하나 받음
선물 지수는 선물을 준 수에서 받은 수를 뺀 거
선물 지수도 같다면 선물 주고받지 않음
다음 달에 선물 주고받을 때 선물을 가장 많이 받을 친구가 받을 선물의 수를 구해라

친구들의 이름을 담은 1차원 문자열 배열 friends
이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts
*/

#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

vector<string> split(string input, char dlim)
{
	vector<string> result;

	stringstream ss;
	string stringBuffer;
	ss.str(input);
	
	while (getline(ss, stringBuffer, dlim))	
	{
		result.push_back(stringBuffer);
	}

	return result;
}

bool cmp(int a, int b) {
    return a > b;
}

int solution(vector<string> friends, vector<string> gifts) {    
    int num = friends.size();
    
    map<string, int> friends_number;
    for (int i = 0; i < num; i++)
    {
        friends_number[friends[i]] = i;
    }
    
    // 사람 별 선물 지수
    int gift_index[50] = {};
    // 선물을 누가 누구에게 줬는지
    int give[50][50] = {};
    // 다음 달 선물 받는 개수
    int next_gift[50] = {};  
 
    for (string gift : gifts) 
    {
        vector<string> v = split(gift, ' ');
        
        int g = friends_number[v[0]];
        int t = friends_number[v[1]];
        
        gift_index[g]++;
        gift_index[t]--;
        
        give[g][t]++;
    }
      
    for (int i = 0; i < num; i++)
    {
        for (int j = i+1; j < num; j++)
        {
            if (i != j)
            {
                if (give[i][j] > give[j][i])
                {
                    next_gift[i]++;
                }
                else if (give[i][j] < give[j][i])
                {
                    next_gift[j]++;
                }
                else
                {
                    if (gift_index[i] > gift_index[j])
                    {   
                        next_gift[i]++;
                    }
                    else if (gift_index[i] < gift_index[j])
                    {   
                        next_gift[j]++;
                    }
                }
            }
        }
    }
    
    sort(next_gift, next_gift + num, cmp);
    
    return next_gift[0];
}