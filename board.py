from pieces import *


class Board:
    #WARNING: PLESAE USE LINUX, APPARENTLY WINDOWS CAN'T RECOGNISE THE ASCII PROVIDED BY YOU.
    #I COULDN'T FIGURE OUT HOW TO ENABLE SUCH ASCII ON WINDOWS.
    def __init__(self):
        self.gameBoard = [["[   ]" for y in range(9)] for x in range(9)]
        for i in range(0, 8):
            self.gameBoard[0][i + 1] =f"( {i + 1} )"
            self.gameBoard[i + 1][0] = f"({chr(65+ i)})"
        self.placePieces()


    def placePieces(self):
        backLineOfWhite = [Rook("White",self,('H',1)), Knight("White",self,('H',2)), Bishop("White",self,('H',3))
            , Queen("White",self,('H',4)), King("White",self,('H',5)), Bishop("White",self,('H',6))
            , Knight("White",self,('H',7)), Rook("White",self,('H',8))]
        backLineOfBlack = [Rook("Black",self,('A',1)), Knight("Black",self,('A',2)), Bishop("Black",self,('A',3))
            , Queen("Black",self,('A',4)), King("Black",self,('A',5)), Bishop("Black",self,('A',6))
            , Knight("Black",self,('A',7)), Rook("Black",self,('A',8))]
        for i in range(1, 9):
            self.gameBoard[1][i] = backLineOfBlack[i - 1]
            self.gameBoard[2][i] = Pawn("Black",self,('B',i))
            self.gameBoard[8][i] = backLineOfWhite[i - 1]
            self.gameBoard[7][i] = Pawn("White",self,("G",i))
        self.gameBoard[0][0] = "   "

    def setPiece(self, position, piece):
        self.gameBoard[position[0]][position[1]] = piece

    def getPiece(self, position):
        chars=["A","B","C","D","E","F","G","H","1","2","3","4","5","6","7","8","[   ]"]
        if not isinstance(self.gameBoard[position[0]][position[1]],str):
            return self.gameBoard[position[0]][position[1]]
        return None

    # ---------------------------------------------------------------------------------------------------------------------

    def makeMove(self, startPosition, endPosition, player):
        if self.getPiece(startPosition)!=None:
            if (self.getPiece(startPosition).getIcon() in whiteIcons.values()) and player == "White" or \
                    (self.getPiece(startPosition).getIcon() in blackIcons.values()) and player == "Black":
                return self.getPiece(startPosition).move(endPosition)

        return False

    # ---------------------------------------------------------------------------------------------------------------------

    def displayBoard(self):
        for i in range(0, 9):
            print(' '.join([f"[{self.getPiece((i,j)).getIcon()}]" if not self.getPiece((i,j))==None
                            else self.gameBoard[i][j] for j in range(0, 9)]))
