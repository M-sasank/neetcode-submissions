class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_map<char,int>> boxes(9);
        for(int i=0;i<9;i++){
            unordered_map<char,int> column_count;
            unordered_map<char,int> row_count;
            for(int j=0;j<9;j++){
                if(board[i][j] != '.'){
                if (row_count.find(board[i][j])!=row_count.end()){
                    return false;
                }
                    row_count[board[i][j]]++;
                if (boxes[(i/3)*3+(j/3)].find(board[i][j])!=boxes[(i/3)*3+(j/3)].end()){
                    return false;
                }
                boxes[(i/3)*3+(j/3)][board[i][j]]++;
                }
                if(board[j][i] != '.') {
                    if (column_count.find(board[j][i])!=column_count.end()){
                    return false;
                    }
                column_count[board[j][i]]++;
                }
            }
        }
        return true;
        
    }

};
