import chess

piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def evaluate(board):
    white_material = 0
    black_material = 0
    
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values.get(piece.piece_type, 0)
            if piece.color == chess.WHITE:
                white_material += value
            else:
                black_material += value
    
    return white_material - black_material

def minimax(board, depth, maximizing_player, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board, depth - 1, False, alpha, beta))
            board.pop()
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, depth - 1, True, alpha, beta))
            board.pop()
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def main():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        
        if board.turn == chess.WHITE:
            move = input("Entre ton coup (ex : e2e4): ")
            if chess.Move.from_uci(move) in board.legal_moves:
                board.push(chess.Move.from_uci(move))
            else:
                print("Coup illégal ! Essaie encore.")
        else:
            best_move = None
            best_value = -float('inf')
            for move in board.legal_moves:
                board.push(move)
                move_value = minimax(board, 3, False)
                if move_value > best_value:
                    best_value = move_value
                    best_move = move
                board.pop()
            print(f"Le moteur joue : {best_move}")
            board.push(best_move)
        
    print("Partie terminée!")
    print("Résultat : ", board.result())

if __name__ == "__main__":
    main()
