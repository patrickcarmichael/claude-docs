---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Output

```python
def solve_sudoku(grid):
   def is_valid(row, col, num):
       # Check if the number is valid in the current row and column

       for i in range(9):
           if grid[row][i] == num or grid[i][col] == num:
               return False

       # Check if the number is valid in the current 3x3 subgrid

       start_row, start_col = (row // 3) * 3, (col // 3) * 3
       for i in range(3):
           for j in range(3):
               if grid[start_row + i][start_col + j] == num:
                   return False

       return True

   def backtrack(row, col):
       # If we have filled all cells, the puzzle is solved

       if row == 9:
           return True

       # Move to the next row if we have reached the end of the current row

       if col == 9:
           return backtrack(row + 1, 0)

       # If the current cell is already filled, move to the next cell

       if grid[row][col] != 0:
           return backtrack(row, col + 1)

       # Try filling the current cell with numbers from 1 to 9

       for num in range(1, 10):
           if is_valid(row, col, num):
               grid[row][col] = num
               if backtrack(row, col + 1):
                   return True
               grid[row][col] = 0

       # If no valid number is found, backtrack

       return False

   # Validate the input grid

   if not all(len(row) == 9 and all(0 <= cell <= 9 for cell in row) for row in grid):
       return None

   # Start the backtracking algorithm

   if backtrack(0, 0):
       return grid
   else:
       return None
```
***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
