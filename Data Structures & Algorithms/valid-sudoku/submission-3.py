class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{}  for _ in range(9)]
        cols = [{}  for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": continue

                k = (i // 3) * 3 + (j // 3)  # 0–8, which box

                # check all 3 maps
                if val in rows[i] or val in cols[j] or val in boxes[k]:
                    return False

                rows[i][val]   = 1
                cols[j][val]   = 1
                boxes[k][val]  = 1

        return True