__author__ = 'anna'

board=[]
def computer_move(board,computer,human):
    board=board[:]
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    for c_move in legal_moves(board):
        board[c_move]==computer
        if winner(board)==computer:
            print(c_move)
        board[c_move]=EMPTY
    for h_move in legal_moves(board):
        board[h_move]=human
        if winner(board)==human:
            print h_move
        board[h_move]=EMPTY
    for b_move in BEST_MOVES:
        if b_move in legal_moves(board):
            print b_move
    if c_move:
        return c_move
        print c_move
    elif h_move:
        return h_move
        print h_move
    else:
        return b_move
        print b_move


