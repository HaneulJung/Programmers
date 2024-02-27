/*
색깔이 담긴 2차원 문자열 리스트 board
칸의 위치를 나타내는 두 정수 h, w

board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수 return
*/

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    
    int width = board.size();
    int height = board[0].size();
    
    vector<vector<int>> check = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    for (int i = 0; i < check.size(); i++)
    {
        if (h+check[i][0] >= 0 && h+check[i][0] < height &&
           w+check[i][1] >= 0 && w+check[i][1] < width)
        {   
            if (board[h+check[i][0]][w+check[i][1]] == board[h][w])
            {
                answer++;    
            }
        }
    }
    
    return answer;
}