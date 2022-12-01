def sudoku(puzzle):

    for row, col in [(r, c) for r in range(9) for c in range(9) if not puzzle[r][c]]:
            
        rr, cc = (row // 3) * 3, (col // 3) * 3
            
        use = {1,2,3,4,5,6,7,8,9} - ({puzzle[row][c] for c in range(9)} | {puzzle[r][col] for r in range(9)} | {puzzle[rr+r][cc+c] for r in range(3) for c in range(3)})

        if len(use) == 1:
            puzzle[row][col] = use.pop()
            return sudoku(puzzle)
    return puzzle

#https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python