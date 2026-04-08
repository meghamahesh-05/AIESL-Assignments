board=[' ']*9

def show():
    print()
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def winner():
    wins=[(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c]and board[a]!=' ':
            return board[a]
    if ' ' not in board:
        return "draw"
    return None

def minimax(is_max): #is_max can be true or false for X and O resp
    w=winner()
    if w=='X': return 1
    if w=='O': return -1
    if w=='draw': return 0

    if is_max:
        best=-100
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                best=max(best,minimax(False))
                board[i]=' '
        return best
    else:
        best=100
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                best=min(best,minimax(True))
                board[i]=' '
        return best

def ai_move():
    best=-100
    move=0
    for i in range(9):
        if board[i]==' ':
            board[i]='X'
            score=minimax(False)
            board[i]=' '
            if score > best:
                best=score
                move=i
    return move

print("Positions 0-8")

while True:
    show()
    m=int(input("Your move: "))
    if board[m]!= ' ':
        print("Invalid!")
        continue
    board[m]='O'
    if winner(): break
    board[ai_move()]='X'
    if winner(): break
show()
res=winner()
if res=='X':
    print("AI wins")
elif res=='O':
    print("You win")
else:
    print("Draw")