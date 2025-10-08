# MinesweeperGameBoard
This is a fork of Minsweeper Game Board implementing the first step

## Meetings
**Wednesdays from 4:00 PM - 5:00 PM in Eaton 3010**

## Collaboration Guidelines
Since this is a group project, **all pull requests will be discussed and decided**
When contributing code, please keep in mind the following:
- **Work in a branch**: Always create a new branch for your feature or bug fix.
  - Example: `feature/mine-counter` or `bigfix/reset-button`
- **Protected main branch**: The `main` branch is protected. All changes must come through a pull request
  - These will be discussed at meetings
  - This ensures the codebase stays stable and that everyone understands new changes
- **Pull requests**: Use PRs to submit your work. They serve as a place for discussion, feedback, and approval
- **Comment your code**: Write clear, helpful comments so the whole team can follow your work.
  - Keep your commits clear and concise.
  - Be respectful of others' contributions and open to feedback.
- **Consistency**: Stick to the project's coding style so the codebase stays uniform.

## Example of Well-Commented Code

```Python
# Function to calculate the number of adjacent mines for a given cell
def count_adjacent_mines(board,row,col);
  mine_count =0
  # Loop through all neighboring cells (3x3 grid centered on [row][col])
  for i in range (row-1, row + 2):
    for j in range (col - 1, col + 2):
      # Ensure we stay within board boundaries
      if 0 <= i < len(board) and 0 <= j < len(board[0]):
        # Skip the current cell
        if (i, j) != (row, col):
          if board[i][j] == "M": # "M" represents a mine
            mine_count += 1
  return mine_count
