import numpy
N = input(int(("Please pick an integer N to make a N columns for Board:\n")))
M = input(int(("Please pick an integer M to make M rows for Board:\n")))

print("The Chess Board You Have Selected Is A", N,"x",M, "Board!")

class NAdjustedKing:

    "the board size and number of solutions"
    #Dont know how to get board to work
    def initialBoard(row, column):
        row = M
        col = N
        size = 
        self.size = size
        self.solutions = 0
        self.solve()
        
    "solve the problem and print num solutions"
    def solve(self):
        positions = [-1] * self.size
        self.place_king(positions, 0)
        print("Found", self.solutions, "solutions!")
        
    "Place the king on a row and check N cases.  If a valid solutuon
    #Cant get the king to work
    def put_king(self, positions, target_row, taget_col):
        for target_row in range(1:M):
            if target_row = M:
                for target_col in range(1:N):
                    if target_col = N:
                        self.show_full_board(positions)
                        self.solutuions += 1
                    else:
                        for target_col in range(1:N):
                            if col = N:
                                return;
                    else:
                        
