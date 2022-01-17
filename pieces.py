blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:
    #WARNING: PLESAE USE LINUX, APPARENTLY WINDOWS CAN'T RECOGNISE THE ASCII PROVIDED BY YOU.
    #I COULDN'T FIGURE OUT HOW TO ENABLE SUCH ASCII ON WINDOWS.
    def __init__(self, color, board, position):
        self.Color = color
        self.__board = board
        self.Position = position

    @property
    def color(self):
        return self.Color

    @property
    def position(self):
        return self.Position

    @position.setter
    def position(self, position):
        if 96 < ord(position[0]) < 105 and 0 < position[1] < 9:
            self.position = position

    def getBoard(self):
        return self.__board

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False

    def getName(self):
        return self.__class__.__name__

    def getIcon(self):
        return None


# ---------------------------------------------------------------------------------------------------------------------

class Knight(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if ((J - newJ == 2 or J - newJ == -2) and (I - newI == 1 or I - newI == -1)) or \
                ((I - newI == 2 or I - newI == -2) and (J - newJ == 1 or J - newJ == -1)):
            if self.getBoard().getPiece((newJ, newI)) is None or (
                    self.getBoard().getPiece((newJ, newI)) is not None and \
                    self.color != self.getBoard().getPiece((newJ, newI)).color):
                return True
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]


# ---------------------------------------------------------------------------------------------------------------------
class Rook(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if (J - newJ != 0 and I - newI != 0) or (J - newJ == 0 and I - newI == 0) or (
                self.getBoard().getPiece((newJ, newI)) is not None and \
                self.color == self.getBoard().getPiece((newJ, newI)).color):
            return False
        elif J - newJ == 0:
            for i in range(min(I, newI) + 1, max(I, newI)):
                if self.getBoard().getPiece((J, i)) is not None:
                    return False
        elif I - newI == 0:
            for j in range(min(J, newJ) + 1, max(J, newJ)):
                if self.getBoard().getPiece((j, I)) is not None:
                    return False
        return True

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]


# ---------------------------------------------------------------------------------------------------------------------

class Bishop(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if ((J - newJ) * (J - newJ) != (I - newI) * (I - newI) or J - newJ == 0) or (
                self.getBoard().getPiece((newJ, newI)) is not None and \
                self.color == self.getBoard().getPiece((newJ, newI)).color):
            return False
        else:
            for j in range(min(J, newJ) + 1, max(J, newJ)):
                for i in range(min(I, newI) + 1, max(I, newI)):
                    if (j - newJ) * (j - newJ) == (i - newI) * (i - newI) and self.getBoard().getPiece(
                            (j, i)) is not None:
                        return False
        return True

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]


# ---------------------------------------------------------------------------------------------------------------------

class Queen(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if ((J - newJ) * (J - newJ) != (I - newI) * (I - newI) and I - newI != 0 and J - newJ != 0) or (
                I - newI == 0 and J - newJ == 0) or (
                self.getBoard().getPiece((newJ, newI)) is not None and \
                self.color == self.getBoard().getPiece((newJ, newI)).color):
            return False
        elif I - newI == 0:
            for j in range(min(J, newJ) + 1, max(J, newJ)):
                if self.getBoard().getPiece((j, I)) is not None:
                    return False
        elif J - newJ == 0:
            for i in range(min(I, newI) + 1, max(I, newI)):
                if self.getBoard().getPiece((J, i)) is not None:
                    return False
        else:
            for j in range(min(J, newJ) + 1, max(J, newJ)):
                for i in range(min(I, newI) + 1, max(I, newI)):
                    if (j - newJ) * (j - newJ) == (i - newI) * (i - newI) and self.getBoard().getPiece(
                            (j, i)) is not None:
                        return False
        return True

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]


# ---------------------------------------------------------------------------------------------------------------------

class King(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if ((abs(J - newJ) == 1 and abs(I - newI) == 1) or (abs(J - newJ) == 1 and abs(I - newI) == 0) or \
            (abs(J - newJ) == 0 and abs(I - newI) == 1)) \
            and ((self.getBoard().getPiece((newJ, newI)) is None or (
                self.getBoard().getPiece((newJ, newI)) is not None and \
                self.color != self.getBoard().getPiece((newJ, newI)).color))):
            return True
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]


# ---------------------------------------------------------------------------------------------------------------------

class Pawn(Piece):
    def checkMove(self, dest):
        newJ = ord(dest[0]) - 64
        newI = int(dest[1])
        J = ord(self.position[0]) - 64
        I = self.position[1]
        if (newI - I == 1 or newI - I == -1) and (J - newJ == 1 if self.color == "White" else -1) and \
                self.getBoard().getPiece((newJ, newI)) is not None and \
                self.color != self.getBoard().getPiece((newJ, newI)).color:
            return True
        if (J - newJ != 1 and self.color == "White") or (newJ - J != 1 and self.color == "Black") or \
                (newI - I != 0) or self.getBoard().getPiece((newJ, newI)) is not None:
            return False
        print(self.getBoard().getPiece((newJ, newI)))
        return True

    def move(self, dest):
        if self.checkMove(dest):
            self.getBoard().setPiece((ord(dest[0]) - 64, int(dest[1])), self)
            self.getBoard().setPiece((ord(self.position[0]) - 64, self.position[1]), "[   ]")
            self.Position = (dest[0], int(dest[1]))
            return True
        return False

    def getIcon(self):
        return whiteIcons[self.getName()] if self.color == "White" else blackIcons[self.getName()]
