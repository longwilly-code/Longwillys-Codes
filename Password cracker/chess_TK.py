import tkinter as tk

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color


selected = None

square_size = 100

board = [[None for _ in range(8)] for _ in range(8)]


# -- makes the board visual
def draw_board():
    

    for row in range(8):
        for col in range(8):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            color = "light blue" if (col + row) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)




# -- start positions for the pieces
def setup_board():
    # pawns
    for col in range(8):
        board[1][col] = Piece("pawn", "black")
        board[6][col] = Piece("pawn", "white")


    # rooks
    board[0][0] = board[0][7] = Piece("rook", "black")
    board[7][0] = board[7][7] = Piece("rook", "white")


    # Knights
    board[0][1] = board[0][6] = Piece("knight", "black")
    board[7][1] = board[7][6] = Piece("knight", "white")

    # Bishops
    board[0][2] = board[0][5] = Piece("bishop", "black")
    board[7][2] = board[7][5] = Piece("bishop", "white")

    # Queens
    board[0][3] = Piece("queen", "black")
    board[7][3] = Piece("queen", "white")

    # Kings
    board[0][4] = Piece("king", "black")
    board[7][4] = Piece("king", "white")



def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                x = col * square_size + square_size // 2
                y = row * square_size + square_size // 2


                symbol = piece.type[0].upper()
                if piece.type == "knight":
                    symbol = "N"


                color = "black" if piece.color == "black" else "white" 

                canvas.create_text(x, y, text=symbol, fill=color, font=("Arial", 24))


def on_click(event):
    global selected
    col = event.x // square_size
    row = event.y // square_size

    print(f"clikced: row={row}, col={col}")

    piece = board[row][col]
    if selected is None:
        if piece:
            selected = (row, col)
            print(f"selected: {piece.type}")
    else:
        print("Move to:", row, col)
        selected = None

    from_row, from_col = selected
    if is_valid_move(from_row, from_col, row, col):
        board[row][col] = board[from_row][from_col]
        board[from_row][from_col] = None
    selected = None


# --- checks if a move is valid. fr = from row | fc = from col | tr = to row | tc = to col
def is_valid_move(fr, fc, tr, tc):
    piece = board[fr][fc]
    
    if piece.type == "pawn":
        return is_valid_pawn_move(piece, fr, fc, tr, tc)
    return False



def is_valid_pawn_move(piece, fr, fc, tr, tc):
    direction = -1 if piece.color == "white" else 1

    # --- basic move
    if fc == tc and tr == fr + direction and board[tr][tc] is None:
        return True
    

    # --- move 2 at start
    start_row = 6 if piece.color == "white" else 1
    if (fr == start_row
        and fc == tc
        and tr == fr + 2 * direction
        and board[fr + direction][tc] is None
        and board[tr][tc] is None):
        return True
    
    if abs(fc - tc) == 1 and tr == fr + direction:
        target = board[tr][tc]
        if target and target.color != Piece.color:
            return True
        
    return False
    



# --- GUI ---

root = tk.Tk()
root.title("Chess")
root.geometry("800x800")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
canvas.bind("<Button-1>", on_click)


canvas.delete("all")
setup_board()
draw_board()
draw_pieces()
root.mainloop()