import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.Font(None, 60)

# Board Setup
board = [' ' for _ in range(9)]

# Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

def draw_lines():
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            index = row * 3 + col
            if board[index] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 ((col + 1) * SQUARE_SIZE - SPACE, (row + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SPACE, (row + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[index] == 'O':
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                   row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_win():
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != ' ':
            return board[i * 3]
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
    if ' ' not in board:
        return 'Draw'
    return None

def alpha_beta(is_maximizing, alpha, beta):
    winner = check_win()
    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10
    elif winner == 'Draw':
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alpha_beta(False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = alpha_beta(True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def computer_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alpha_beta(False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = 'O'

def draw_winner(text):
    winner_text = FONT.render(text, True, BLUE)
    screen.blit(winner_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)

def reset_game():
    global board, player_turn
    board = [' ' for _ in range(9)]
    player_turn = True
    screen.fill(WHITE)
    draw_lines()

# Main game loop
draw_lines()
player_turn = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            cell = (event.pos[1] // SQUARE_SIZE) * 3 + (event.pos[0] // SQUARE_SIZE)
            if board[cell] == ' ':
                board[cell] = 'X'
                player_turn = False
                if check_win() is None:
                    computer_move()
                    player_turn = True
    screen.fill(WHITE)
    draw_lines()
    draw_figures()
    pygame.display.update()
    winner = check_win()
    if winner:
        draw_winner(f"Results: {winner}")
        reset_game()

pygame.quit()
