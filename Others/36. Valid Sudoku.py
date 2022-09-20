class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        line_num, col_num = 9, 9
        
        line_sets = [set() for _ in range(line_num)]
        col_sets = [set() for _ in range(col_num)]
        sq_sets = [set() for _ in range((col_num // 3) * (line_num // 3))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                item = board[i][j]
                if item.isdigit():
                    # line
                    if item in line_sets[i]:
                        return False
                    else:
                        line_sets[i].add(item)
                    # column
                    if item in col_sets[j]:
                        return False
                    else:
                        col_sets[j].add(item)
                    # square
                    idx = (i // 3) * (col_num // 3) + j // 3
                    if item in sq_sets[idx]:
                        return False
                    else:
                        sq_sets[idx].add(item)
        
        return True
                    

        
        