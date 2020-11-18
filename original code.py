N = input(int(("Please pick an integer N to make a N columns for Board:\n")))
M = input(int(("Please pick an integer M to make M rows for Board:\n")))

print("The Chess Board You Have Selected Is A", N,"x",M, "Board!")

class NAdjustedKing:

    "the board size and number of solutions"
    def initialBoard(self, size):
        size = N
        self.size = size
        self.solutions = 0
        self.solve()
        
    "solve the problem and print num solutions"
    def solve(self):
        positions = [-1] * self.size
        self.place_king(positions, 0)
        print("Found", self.solutions, "solutions!")
        
    "Place the king on a row and check N cases.  If a valid solutuon
    
        
