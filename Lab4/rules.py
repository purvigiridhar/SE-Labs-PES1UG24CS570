SIZE = 8


def simple_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    direction = -1 if player == "R" else 1
    return (
        board[er][ec] == "." and
        abs(er - sr) == 1 and abs(ec - sc) == 1 and
        (piece in ("RK", "BK") or er - sr == direction)
    )


def capture_move(board, player, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    direction = -1 if player == "R" else 1
    mr, mc = (sr + er) // 2, (sc + ec) // 2
    return (
        board[er][ec] == "." and
        abs(er - sr) == 2 and abs(ec - sc) == 2 and
        (piece in ("RK", "BK") or er - sr == 2 * direction) and
        board[mr][mc] not in (".", player)
    )


def has_pieces(board, player):
    return any(
        cell in (player, player + "K")
        for row in board
        for cell in row
    )


def has_capture_from(board, player, start):
    sr, sc = start
    for er in range(SIZE):
        for ec in range(SIZE):
            if capture_move(board, player, start, (er, ec)):
                return True
    return False


def has_capture(board, player):
    for sr in range(SIZE):
        for sc in range(SIZE):
            if board[sr][sc] not in (player, player + "K"):
                continue
            if has_capture_from(board, player, (sr, sc)):
                return True
    return False


def has_legal_moves(board, player):
    for sr in range(SIZE):
        for sc in range(SIZE):
            if board[sr][sc] not in (player, player + "K"):
                continue
            for er in range(SIZE):
                for ec in range(SIZE):
                    start, end = (sr, sc), (er, ec)
                    if capture_move(board, player, start, end):
                        return True
                    if simple_move(board, player, start, end):
                        return True
    return False


def promote(board):
    for c in range(SIZE):
        if board[0][c] == "R":
            board[0][c] = "RK"
        if board[SIZE - 1][c] == "B":
            board[SIZE - 1][c] = "BK"
