using System;

public class Solution {
    public int solution(string[] babbling) {
        int answer = 0;        
        
        for (int i = 0; i < babbling.Length; i++){
            string[] can = {"aya", "ye", "woo", "ma"};
            for (int j = 0; j < can.Length; ++j){
                Console.WriteLine($"{i}, {j}, {babbling[i].IndexOf(can[j])}");
                
                if (babbling[i].IndexOf(can[j]) == 0){                    
                    babbling[i] = babbling[i].Replace(can[j], "");
                    can[j] = "*";
                    j = -1;
                }
            }            
            if (babbling[i] == ""){
                answer += 1;
            }
        }
        
        return answer;
    }
}