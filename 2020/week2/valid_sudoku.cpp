// By Ba Nguyen Nguyen

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Can use bitarrays here but too lazy
        vector<set<int>> rows(9);
        vector<set<int>> cols(9);
        vector<set<int>> squares(9);
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    auto r = rows[i].insert(board[i][j]);
                    auto c = cols[j].insert(board[i][j]);
                    auto s = squares[3 * (i/3) + j/3].insert(board[i][j]);
                    // returns smth like pair<iterator, bool>
                    //                                   /\_ is inserted
                    if (!r.second || !c.second || !s.second) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};