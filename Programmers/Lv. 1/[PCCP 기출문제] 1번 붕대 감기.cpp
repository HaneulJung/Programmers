/*
t초 동안 붕대를 감으면서 1초마다 x만큼 체력을 회복
t초 연속으로 붕대를 감는 데 성공했다면 y만큼 추가로 회복
공격을 당하는 순간 체력 회복 불가
캐릭터가 끝까지 생존할 수 있는지 궁금

붕대감기 시전 시간, 1초당 회복량, 추가 회복량 담은 1차원 정수 배열 bandage
최대 체력 health
몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 attacks
모든 공격이 끝난 후 남은 체력을 return
*/

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int cur_health = health;
    
    int cur_time = 0;
    int prev_time = 0;
    
    for (int i = 0; i < attacks.size(); i++)
    {
        cur_time = attacks[i][0];            
                
        // 경과 시간 기본 회복
        int elapsed_time = cur_time - prev_time - 1;
        cur_health += elapsed_time * bandage[1];
                
        // 연속 성공 추가 회복
        cur_health += (elapsed_time / bandage[0]) * bandage[2];     
        
        // 최대 체력보다 커지면 최대 체력으로 다시 설정
        if (cur_health >= health)
        {
            cur_health = health;
        }
        
        // 공격 피해
        cur_health -= attacks[i][1];
        
        if (cur_health <= 0)
        {
            return -1;
        }
        
        // 이전 시간을 다시 세팅
        prev_time = cur_time;    
    }
    
    return cur_health;
}