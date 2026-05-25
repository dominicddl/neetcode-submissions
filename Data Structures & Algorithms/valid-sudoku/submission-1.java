class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Initialise Row Hash Map
        Map<Integer, Set<Character>> rows = new HashMap<>();
        
        // Initialise Column Hash Map
        Map<Integer, Set<Character>> columns = new HashMap<>();

        // Initialise Sub-Box Hash Map 
        Map<Integer, Set<Character>> subBoxes = new HashMap<>();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }

                int subIdx = (i / 3) * 3 + (j / 3);
                if (rows.computeIfAbsent(i, x -> new HashSet<>()).contains(board[i][j])
                || columns.computeIfAbsent(j, x -> new HashSet<>()).contains(board[i][j])
                || subBoxes.computeIfAbsent(subIdx, x -> new HashSet<>()).contains(board[i][j])) {
                    return false;
                }
                rows.get(i).add(board[i][j]);
                columns.get(j).add(board[i][j]);
                subBoxes.get(subIdx).add(board[i][j]);
            }
        }
        return true;
    }
}
