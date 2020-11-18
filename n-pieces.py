"""The N-pieces puzzle"""

# Further changes - mkings checking, noard array, changing board size, other pieces, etc.


class NPieces:
    """Generate all solutions for N-pieces puzzle for specified piece and board size"""
    def __init__(self, size, piece):
        # Store the puzzle (problem) size and the number of valid solutions
        # add - row, col, num-pieces
        self.size = size
        self.piece = piece
        self.solutions = 0
        self.solve()

    def solve(self):
        """Solve the N-pieces puzzle and print the number of solutions"""
        positions = [-1] * self.size
        if self.piece == "q" or "Q":
            self.put_queen(positions, 0)
        else:
            if self.piece == "r" or "R":
                self.put_rook(positions, 0)
            else:
                if self.piece == "k" or "K":
                    self.put_king(positions, 0)
                else:
                    if self.piece == "b" or "B":
                        self.put_bishop(positions,0)
                    
        print("Found ", self.solutions, " solutions.")
        print("Press the <ENTER> key to continue...")
        input()

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the functions recurses trying to place a queen
        on the next row until all N pieces are placed on the NxN board.
        """
        # Base case - all N rows are occupied
        if target_row == self.size:
             self.show_full_board(positions)
             self.solutions += 1
        else:
             # For all N columns positions try to place a queen
             for column in range(self.size):
                 # Reject all invalid positions
                 if self.check_place_queen(positions, target_row, column):
                     positions[target_row] = column
                     self.put_queen(positions, target_row + 1)


    def put_rook(self, positions, target_row):
        """
        Try to place a rook on target_row by checking all N possible cases.
        If a valid place is found the functions recurses trying to place a rook
        on the next row until all N pieces are placed on the NxN board.
        """
        # Base case - all N rows are occupied
        if target_row == self.size:
             self.show_full_board(positions)
             self.solutions += 1
        else:
             # For all N columns positions try to place a rook
             for column in range(self.size):
                 # Reject all invalid positions
                 if self.check_place_rook(positions, column):
                     positions[target_row] = column
                     self.put_rook(positions, target_row + 1)

    def put_bishop(self, positions, target_row):
        """
        Try to place a bishop on target_row by checking all N possible cases.
        If a valid place is found the functions recurses trying to place a bishop
        on the next row until all N pieces are placed on the NxN board.
        """
        # Base case - all N rows are occupied
        if target_row == self.size:
             self.show_full_board(positions)
             self.solutions += 1
        else:
             # For all N columns positions try to place a bishop
             for column in range(self.size):
                 # Reject all invalid positions
                 if self.check_place_bishop(positions, target_row, column):
                     positions[target_row] = column
                     self.put_bishop(positions, target_row + 1)

    def put_king(self, positions, target_row):
        """
        Try to place a king on target_row by checking all N possible cases.
        If a valid place is found the functions recurses trying to place a king
        on the next row until all N pieces are placed on the NxN board.
        """
        # Base case - all N rows are occupied
        if target_row == self.size:
             self.show_full_board(positions)
             self.solutions += 1
        else:
             # For all N columns positions try to place a queen
             for column in range(self.size):
                 # Reject all invalid positions
                 if self.check_place_king(positions, target_row, column):
                     positions[target_row] = column
                     self.put_king(positions, target_row + 1)

    def put_mking(self, positions, target_row):
        """
        Try to place a mking on target_row by checking all N possible cases.
        If a valid place is found the functions recurses trying to place a mking
        on the next row until all N pieces are placed on the NxN board.
        """
        # Base case - all N rows are occupied
        if target_row == self.size:
             self.show_full_board(positions)
             self.solutions += 1
        else:
             # For all N columns positions try to place a queen
             for column in range(self.size):
                 # Reject all invalid positions
                 if self.check_place_mking(positions, target_row, column):
                     positions[target_row] = column
                     self.put_mking(positions, target_row + 1)
    

    def check_place_queen(self, positions, occupied_rows, column):
         """
         Check if a given position is under attack from any of
         the previously placed queens (check column and diagonal positions)
         """
         for i in range(occupied_rows):
             if positions[i] == column or \
                positions[i] - i == column - occupied_rows or \
                positions[i] + i == column + occupied_rows:
                return False
         return True

    def check_place_rook(self, positions, column):
         """
         Check if a given position is under attack from any of
         the previously placed rooks (check column)
         """
         if positions[i] == column:
            return False
         return True

    def check_place_bishop(self, positions, occupied_rows, column):
         """
         Check if a given position is under attack from any of
         the previously placed queens (check diagonal positions)
         """
         for i in range(occupied_rows):
             if positions[i] - i == column - occupied_rows or \
                positions[i] + i == column + occupied_rows:
                return False
         return True


    def check_place_king(self, positions, occupied_rows, column):
         """
         Check if a given position is under attack from any of
         the previously placed kings (check column and diagonal positions)
         """
         for i in range(occupied_rows):
             if positions[i] == column or \
                positions[i] - i == column - occupied_rows or \
                positions[i] + i == column + occupied_rows:
                return False
         return True


    def check_place_mking(self, positions, occupied_rows, column):
         """
         Check if a given position is under attack from any of
         the previously placed mkings (check column positions)
         """
         for i in range(occupied_rows):
             if positions[i] == column:
                return False
         return True
 
    def show_full_board(self, positions):
         """Show the full NxN board"""
         for row in range(self.size):
             line = ""
             for column in range(self.size):
                 if positions[row] == column:
                     line = line + self.piece + " "     
                 else:
                     line += ". "
             print(line)
         print("\n")
        
"""
def main():
    # Initialize and solve the n-pieces puzzle
    NPieces(8,"Q")
    if __name__ == "__main__":
        # execute only if run as a script
        main()
"""


def main(size, piece):
    """Initialize and solve the n-pieces puzzle"""
    NPieces(size, piece)
    if __name__ == "__main__":
        # execute only if run as a script
        main(size, piece)
