#include <string>
#include <vector>

using namespace std;

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    
    for (vector<int> ball : balls)
    {
        int min_distance = m*m + n*n;
                
        if (!(startY == ball[1] && startX > ball[0]))
        {      
            // 왼쪽 면 맞았을 때
            min_distance 
                = min(min_distance, 
                      (startX+ball[0])*(startX+ball[0]) + (startY-ball[1])*(startY-ball[1])); 
        }
            
        if (!(startY == ball[1] && startX < ball[0]))
        {      
            // 오른쪽 면 맞았을 때
            min_distance 
                = min(min_distance, 
                      (2*m-startX-ball[0])*(2*m-startX-ball[0]) + (startY-ball[1])*(startY-ball[1]));         
        }    
        
        if (!(startX == ball[0] && startY < ball[1]))
        {  
             // 위쪽 면 맞았을 때
            min_distance 
                = min(min_distance, 
                      (startX-ball[0])*(startX-ball[0]) + (2*n-startY-ball[1])*(2*n-startY-ball[1]));
        }
        
       if (!(startX == ball[0] && startY > ball[1]))
       {  
            // 아래쪽 면 맞았을 때
            min_distance 
                = min(min_distance, 
                    (startX-ball[0])*(startX-ball[0]) + (startY+ball[1])*(startY+ball[1]));  
       }        
        
        answer.push_back(min_distance);
    }
    return answer;
}