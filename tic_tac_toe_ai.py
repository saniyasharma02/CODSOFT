"""
Tic-Tac-Toe AI Using Minimax Algorithm (with Alpha-Beta Pruning)
------------------------------------------------------------------
A Pygame-based Tic-Tac-Toe game where you play against an AI opponent.

Controls:
    Mouse Click     -> Place your mark (you are 'O', player 1)
    R                -> Restart the current round
    1 / 2 / 3        -> Set AI difficulty to Easy / Medium / Hard

The AI ('X', player 2) uses the Minimax algorithm, optimized with
Alpha-Beta Pruning, to always choose the mathematically best move
available on "Hard" difficulty - making it impossible to beat.
"""

import sys
import random
import pygame
import numpy as np

pygame.init()

# ----------------------------------------------------------------------
# COLORS
# ----------------------------------------------------------------------
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BG_COLOR = (28, 28, 28)
TOP_BAR_COLOR = (20, 20, 20)
TEXT_COLOR = (240, 240, 240)
HINT_COLOR = (150, 150, 150)

# ----------------------------------------------------------------------
# BOARD / WINDOW SETTINGS
# ----------------------------------------------------------------------
BOARD_ROWS = 3
BOARD_COLS = 3

WIDTH = 300                       # Width of the playable board
HEIGHT = 300                      # Height of the playable board
TOP_BAR_HEIGHT = 70                # Space reserved for scoreboard/difficulty text
SCREEN_HEIGHT = HEIGHT + TOP_BAR_HEIGHT

LINE_WIDTH = 5
SQUARE_SIZE = WIDTH // BOARD_COLS

CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

# Difficulty levels
DIFFICULTY_EASY = 1
DIFFICULTY_MEDIUM = 2
DIFFICULTY_HARD = 3
DIFFICULTY_NAMES = {DIFFICULTY_EASY: "Easy", DIFFICULTY_MEDIUM: "Medium", DIFFICULTY_HARD: "Hard"}

# All 8 winning lines on a 3x3 board, expressed as (row, col) triples
WIN_LINES = (
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # rows
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # columns
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],                            # diagonals
)

# ----------------------------------------------------------------------
# GLOBAL STATE
# ----------------------------------------------------------------------
screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI - Minimax")
font = pygame.font.SysFont("arial", 18)
small_font = pygame.font.SysFont("arial", 14)

board = np.zeros((BOARD_ROWS, BOARD_COLS), dtype=int)

scores = {1: 0, 2: 0, "draw": 0}     # 1 = Human, 2 = AI
difficulty = DIFFICULTY_HARD


# ----------------------------------------------------------------------
# DRAWING FUNCTIONS
# ----------------------------------------------------------------------
def draw_top_bar():
    """Render the scoreboard, current difficulty, and control hints."""
    pygame.draw.rect(screen, TOP_BAR_COLOR, (0, 0, WIDTH, TOP_BAR_HEIGHT))

    score_text = f"You: {scores[1]}   AI: {scores[2]}   Draws: {scores['draw']}"
    diff_text = f"Difficulty: {DIFFICULTY_NAMES[difficulty]}"
    hint_text = "1/2/3 = Difficulty   R = Restart"

    screen.blit(font.render(score_text, True, TEXT_COLOR), (10, 6))
    screen.blit(font.render(diff_text, True, TEXT_COLOR), (10, 28))
    screen.blit(small_font.render(hint_text, True, HINT_COLOR), (10, 50))


def draw_lines(color=WHITE):
    """Draw the 3x3 grid lines for the board."""
    for i in range(1, BOARD_ROWS):
        y = TOP_BAR_HEIGHT + SQUARE_SIZE * i
        pygame.draw.line(screen, color, (0, y), (WIDTH, y), LINE_WIDTH)
        x = SQUARE_SIZE * i
        pygame.draw.line(screen, color, (x, TOP_BAR_HEIGHT), (x, TOP_BAR_HEIGHT + HEIGHT), LINE_WIDTH)


def draw_figures(color=WHITE):
    """Draw every 'O' (player 1) and 'X' (player 2) currently on the board."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = TOP_BAR_HEIGHT + row * SQUARE_SIZE + SQUARE_SIZE // 2

            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)

            elif board[row][col] == 2:
                offset = SQUARE_SIZE // 4
                pygame.draw.line(screen, color, (center_x - offset, center_y - offset),
                                  (center_x + offset, center_y + offset), CROSS_WIDTH)
                pygame.draw.line(screen, color, (center_x - offset, center_y + offset),
                                  (center_x + offset, center_y - offset), CROSS_WIDTH)


def draw_winning_line(line, color):
    """Draw a thick line straight through the 3 winning cells."""
    start_row, start_col = line[0]
    end_row, end_col = line[2]

    start_pos = (start_col * SQUARE_SIZE + SQUARE_SIZE // 2,
                 TOP_BAR_HEIGHT + start_row * SQUARE_SIZE + SQUARE_SIZE // 2)
    end_pos = (end_col * SQUARE_SIZE + SQUARE_SIZE // 2,
               TOP_BAR_HEIGHT + end_row * SQUARE_SIZE + SQUARE_SIZE // 2)

    pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH + 4)


# ----------------------------------------------------------------------
# GAME STATE HELPERS
# ----------------------------------------------------------------------
def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def get_available_moves(check_board):
    return [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if check_board[r][c] == 0]


def is_board_full(check_board=None):
    if check_board is None:
        check_board = board
    return len(get_available_moves(check_board)) == 0


def get_winning_line(player, check_board=None):
    """Return the winning (row, col) triple for `player`, or None if no win."""
    if check_board is None:
        check_board = board
    for line in WIN_LINES:
        if all(check_board[r][c] == player for r, c in line):
            return line
    return None


def check_win(player, check_board=None):
    return get_winning_line(player, check_board) is not None


# ----------------------------------------------------------------------
# MINIMAX + ALPHA-BETA PRUNING
# ----------------------------------------------------------------------
def minimax(minimax_board, depth, is_maximizing, alpha, beta):
    """
    Recursively evaluate every possible future of the game.

    Returns:
         1  -> if this branch leads to an AI (player 2) win
        -1  -> if this branch leads to a Human (player 1) win
         0  -> if this branch leads to a draw

    `alpha` and `beta` track the best score the maximizer (AI) and
    minimizer (human) can already guarantee elsewhere in the tree -
    once a branch can no longer change the outcome, it is pruned
    (skipped) instead of being fully explored, which is what makes
    Alpha-Beta Pruning faster than plain Minimax.
    """
    if check_win(2, minimax_board):
        return 1
    if check_win(1, minimax_board):
        return -1
    if is_board_full(minimax_board):
        return 0

    if is_maximizing:                       # AI's turn - wants the HIGHEST score
        best_score = -1000
        for row, col in get_available_moves(minimax_board):
            minimax_board[row][col] = 2
            score = minimax(minimax_board, depth + 1, False, alpha, beta)
            minimax_board[row][col] = 0

            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                return best_score            # Prune: human will never allow this branch
        return best_score

    else:                                    # Human's turn - wants the LOWEST score
        best_score = 1000
        for row, col in get_available_moves(minimax_board):
            minimax_board[row][col] = 1
            score = minimax(minimax_board, depth + 1, True, alpha, beta)
            minimax_board[row][col] = 0

            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if alpha >= beta:
                return best_score            # Prune: AI will never allow this branch
        return best_score


def best_ai_move(level):
    """
    Decide and play the AI's move (player 2) based on `level`:

        Easy   -> a random legal move (AI makes mistakes)
        Medium -> 50% optimal / 50% random (beatable, but tricky)
        Hard   -> always the optimal move via Minimax + Alpha-Beta (unbeatable)
    """
    moves = get_available_moves(board)
    if not moves:
        return False

    if level == DIFFICULTY_EASY or (level == DIFFICULTY_MEDIUM and random.random() < 0.5):
        row, col = random.choice(moves)
        mark_square(row, col, 2)
        return True

    best_score = -1000
    move = moves[0]
    for row, col in moves:
        board[row][col] = 2
        score = minimax(board, 0, False, -1000, 1000)
        board[row][col] = 0
        if score > best_score:
            best_score = score
            move = (row, col)

    mark_square(move[0], move[1], 2)
    return True


# ----------------------------------------------------------------------
# GAME FLOW HELPERS
# ----------------------------------------------------------------------
def restart_round():
    """Clear the board for a new round (scoreboard is kept)."""
    global board, game_over, player
    board = np.zeros((BOARD_ROWS, BOARD_COLS), dtype=int)
    game_over = False
    player = 1


def record_result(winner):
    """Update the scoreboard. `winner` is 1, 2, or None for a draw."""
    if winner is None:
        scores["draw"] += 1
    else:
        scores[winner] += 1


def render(winning_line=None, winner=None):
    """Redraw the entire screen for the current frame."""
    screen.fill(BG_COLOR)
    draw_top_bar()

    if winner == 1:
        draw_figures(GREEN)
        draw_lines(GREEN)
    elif winner == 2:
        draw_figures(RED)
        draw_lines(RED)
    elif winner == "draw":
        draw_figures(GRAY)
        draw_lines(GRAY)
    else:
        draw_figures(WHITE)
        draw_lines(WHITE)

    if winning_line:
        line_color = GREEN if winner == 1 else RED
        draw_winning_line(winning_line, line_color)

    pygame.display.update()


# ----------------------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------------------
player = 1
game_over = False


def main():
    global player, game_over, difficulty

    clock = pygame.time.Clock()
    winning_line = None
    winner = None

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_round()
                    winning_line, winner = None, None
                elif event.key == pygame.K_1:
                    difficulty = DIFFICULTY_EASY
                elif event.key == pygame.K_2:
                    difficulty = DIFFICULTY_MEDIUM
                elif event.key == pygame.K_3:
                    difficulty = DIFFICULTY_HARD

            if (event.type == pygame.MOUSEBUTTONDOWN and not game_over
                    and event.pos[1] >= TOP_BAR_HEIGHT):

                mouse_col = event.pos[0] // SQUARE_SIZE
                mouse_row = (event.pos[1] - TOP_BAR_HEIGHT) // SQUARE_SIZE

                if 0 <= mouse_row < BOARD_ROWS and available_square(mouse_row, mouse_col):
                    # --- Human move ---
                    mark_square(mouse_row, mouse_col, player)

                    line = get_winning_line(1)
                    if line:
                        game_over, winning_line, winner = True, line, 1
                        record_result(1)
                    elif is_board_full():
                        game_over, winner = True, "draw"
                        record_result(None)
                    else:
                        # --- AI move (only if the game is still going) ---
                        best_ai_move(difficulty)
                        line = get_winning_line(2)
                        if line:
                            game_over, winning_line, winner = True, line, 2
                            record_result(2)
                        elif is_board_full():
                            game_over, winner = True, "draw"
                            record_result(None)

        render(winning_line, winner)
        clock.tick(30)


if __name__ == "__main__":
    main()
