from board import initial_board, move_piece, SIZE
from rules import simple_move, capture_move, promote, has_pieces, has_legal_moves, has_capture, has_capture_from


class Checkers:
    def __init__(self):
        self.board = initial_board()
        self.player = "R"

    def print_board(self):
        print("\n   " + " ".join(str(c) for c in range(SIZE)))
        for r, row in enumerate(self.board):
            print(f"{r}  " + " ".join(row))

    def game_over(self):
        opponent = "B" if self.player == "R" else "R"

        if not has_pieces(self.board, self.player):
            print(f"{opponent} wins! {self.player} has no pieces remaining.")
            return True

        if not has_pieces(self.board, opponent):
            print(f"{self.player} wins! {opponent} has no pieces remaining.")
            return True

        if not has_legal_moves(self.board, self.player):
            print(f"{opponent} wins! {self.player} has no legal moves.")
            return True

        return False

    def run(self):
        print("Checkers — move: sr sc er ec")
        while True:
            self.print_board()
            if self.game_over():
                return

            raw = input(f"{self.player}> ").strip().lower().split()
            if raw == ["q"]:
                return
            if len(raw) != 4:
                print("Enter four coordinates.")
                continue
            try:
                sr, sc, er, ec = map(int, raw)
            except ValueError:
                print("Coordinates must be numbers.")
                continue
            if not all(0 <= x < SIZE for x in (sr, sc, er, ec)):
                print("Outside board.")
                continue
            if self.board[sr][sc] not in (self.player, self.player + "K"):
                print("That is not your piece.")
                continue

            start, end = (sr, sc), (er, ec)
            capture_required = has_capture(self.board, self.player)

            if capture_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                mr, mc = (sr + er) // 2, (sc + ec) // 2
                self.board[mr][mc] = "."
                promote(self.board)

                if has_capture_from(self.board, self.player, end):
                    continue
            elif not capture_required and simple_move(self.board, self.player, start, end):
                move_piece(self.board, start, end)
                promote(self.board)
            else:
                print("Invalid move.")
                continue

            self.player = "B" if self.player == "R" else "R"
