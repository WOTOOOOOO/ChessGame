from board import Board
from pieces import *


class Chess:
    #WARNING: PLESAE USE LINUX, APPARENTLY WINDOWS CAN'T RECOGNISE THE ASCII PROVIDED BY YOU.
    #I COULDN'T FIGURE OUT HOW TO ENABLE SUCH ASCII ON WINDOWS.
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        self.currentPlayer = "Black" if self.currentPlayer == "White" else "White"

    def isStringValidMove(self, moveStr):
        chars=["A","B","C","D","E","F","G","H"]
        if len(moveStr)==5:
          if moveStr[0].isalpha() and moveStr[3].isalpha() and moveStr[1].isdecimal() and moveStr[4].isdecimal():
             if moveStr[0]in chars and moveStr[3] in chars and 0 < int(moveStr[1]) < 9 and 0 < int(moveStr[4]) < 9:
                return True
        return False

    def play(self):
        while (True):
            self.board.displayBoard()
            inp = input(f"{self.currentPlayer}s Turn, Enter move:")
            if inp.lower() == "exit": break
            while not self.isStringValidMove(inp) or \
                    not self.board.makeMove((ord(inp[0]) - 64, int(inp[1])), (inp[3], inp[4]), self.currentPlayer):
                print("Invalid move")
                inp = input(f"{self.currentPlayer}s Turn, Enter move:")
                if inp.lower() == "exit": break
            if inp.lower() == "exit": break
            while (self.board.getPiece((ord(inp[3]) - 64, int(inp[4]))).getIcon() == "♟" and (ord(inp[3]) - 64)== 1 and
                    self.currentPlayer=="White") or\
                (self.board.getPiece((ord(inp[3]) - 64, int(inp[4]))).getIcon() == "♙" and (ord(inp[3]) - 64)== 8 and
                self.currentPlayer=="Black"):
                prom = input("what would you like to promote to?")
                while prom.lower() not in ["knight","queen","rook","bishop"]:
                    prom = input("what would you like to promote to?")
                if prom.lower() == "knight":
                    self.board.setPiece((ord(inp[3]) - 64, int(inp[4])), Knight(self.currentPlayer, self.board, (inp[3], int(inp[4]))))
                if prom.lower() == "queen":
                    self.board.setPiece((ord(inp[3]) - 64, int(inp[4])), Queen(self.currentPlayer, self.board, (inp[3], int(inp[4]))))
                if prom.lower() == "rook":
                    self.board.setPiece((ord(inp[3]) - 64, int(inp[4])), Rook(self.currentPlayer, self.board, (inp[3], int(inp[4]))))
                if prom.lower() == "bishop":
                    self.board.setPiece((ord(inp[3]) - 64, int(inp[4])), Bishop(self.currentPlayer, self.board, (inp[3], int(inp[4]))))
            self.swapPlayers()




if __name__ == "__main__":
    game = Chess()
    game.play()
