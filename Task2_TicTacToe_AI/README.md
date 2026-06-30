<div align="center">

# ⭕❌ Tic-Tac-Toe AI Using Minimax Algorithm

### An Unbeatable AI Opponent Built with Game Theory, Recursive Search, and Alpha-Beta Pruning

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-00A86B?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![AI: Unbeatable](https://img.shields.io/badge/AI-Unbeatable%20on%20Hard-red?style=for-the-badge)](#-performance-analysis)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](#-contribution-guidelines)

*A human player competes against an AI that never loses — because it isn't guessing, it's exhaustively proving the optimal move using classical game-tree search.*

</div>

---
## 🧩 Introduction

Tic-Tac-Toe is the smallest possible "solved" game in artificial intelligence — every outcome can be computed in advance, which makes it the perfect playground for learning **adversarial search**, the family of algorithms that power decision-making in chess engines, poker bots, and strategy-game AI.

This project implements a fully playable, GUI-based Tic-Tac-Toe game where the opponent is not scripted or random — it's powered by the **Minimax algorithm**, accelerated with **Alpha-Beta Pruning**, so it always makes the mathematically correct decision given the current board state.

---

## 🧭 Project Overview

| | |
|---|---|
| **Type** | Desktop 2-player (Human vs AI) board game |
| **Interface** | Graphical, built with Pygame |
| **AI Core** | Minimax + Alpha-Beta Pruning |
| **Difficulty Modes** | Easy, Medium, Hard (unbeatable) |
| **State Tracking** | Live scoreboard (Wins / Losses / Draws) |
| **Dependencies** | Python standard library + Pygame + NumPy only |
| **Offline?** | ✅ 100% offline, no internet or API required |

The game window displays a live scoreboard and the active difficulty level above a classic 3×3 grid. Players click to place their mark; the AI responds instantly, and the winning combination (if any) is highlighted directly on the board.

---

## ❓ Problem Statement

Build a two-player Tic-Tac-Toe game in which:

- A human player interacts through a graphical interface using mouse input.
- The computer opponent must make **provably optimal decisions** rather than relying on chance or fixed scripts.
- The decision-making process must be **computationally efficient**, since a brute-force search of every possible game state grows quickly even in a game this small.
- The system must correctly detect **wins, losses, and draws** under all valid board configurations, including both diagonals, all rows, and all columns.

---

## 🎯 Objectives

- Implement the **Minimax algorithm** to recursively evaluate all future game states from any board position.
- Optimize the search using **Alpha-Beta Pruning** to eliminate branches that cannot influence the final decision.
- Build a clean, responsive **Pygame GUI** supporting mouse-based interaction.
- Support multiple **AI difficulty levels** to make the game enjoyable for players of all skill levels, not just unbeatable by default.
- Track and display a **persistent scoreboard** across multiple rounds.
- Visually highlight the **winning line** when a game concludes.
- Produce clean, well-commented, beginner-readable Python code suitable for an academic or portfolio submission.

---

## ✨ Features

| Feature | Status | Description |
|---|---|---|
| 🖱️ Interactive GUI | ✅ | Built with Pygame, mouse-driven gameplay |
| 🧑 vs 🤖 Gameplay | ✅ | Human (O) plays against the AI (X) |
| 🧠 Unbeatable AI | ✅ | Minimax guarantees a win or draw on Hard difficulty — never a loss |
| ⚡ Alpha-Beta Pruning | ✅ | Cuts ~97% of search nodes without affecting the outcome (see [Performance Analysis](#-performance-analysis)) |
| 🎮 Difficulty Levels | ✅ | Easy (random), Medium (50/50), Hard (optimal/unbeatable) — switch live with keys `1`/`2`/`3` |
| 🏆 Scoreboard System | ✅ | Tracks wins, losses, and draws across rounds |
| 🔄 Restart Functionality | ✅ | Press `R` to instantly start a new round |
| ✅ Win / Loss / Draw Detection | ✅ | Checks all 8 possible winning lines plus full-board draws |
| 📏 Winning Line Visualization | ✅ | Draws a highlighted line directly through the winning combination |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Pygame** | Window management, rendering, event handling, input |
| **NumPy** | Efficient 2D array representation of the game board |
| **Recursion** | Implementing the Minimax search tree |
| **Game Theory** | Theoretical foundation for adversarial decision-making |

---

## 🧮 Algorithms Used

| Algorithm | Role in This Project |
|---|---|
| **Minimax** | Core decision-making algorithm — recursively simulates every possible continuation of the game to determine the optimal move |
| **Alpha-Beta Pruning** | Optimization layered on top of Minimax that skips branches mathematically guaranteed to never be chosen |
| **Random Selection** | Used only in Easy/Medium difficulty to intentionally weaken the AI for casual play |

---

## 🧠 Minimax Algorithm Explanation

> **Beginner-friendly summary:** Minimax assumes both players play perfectly. It looks at every possible move, then every possible response to that move, all the way to the end of the game — and picks the move that leads to the *best outcome the AI can guarantee*, assuming the human will always try to make things worst for the AI.

**How it works in this project:**

1. The AI (maximizing player, score target = **+1**) considers every empty square.
2. For each candidate move, it simulates placing its mark, then recursively asks: *"If the human now plays optimally to minimize my score, what's the best I can still achieve?"*
3. The human (minimizing player, score target = **−1**) is simulated as always picking the move that's worst for the AI.
4. Each complete game ends in one of three scores:
   - `+1` → AI wins
   - `-1` → Human wins
   - `0` → Draw
5. The AI ultimately picks the move whose simulated future has the **highest guaranteed score**.

```python
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(AI):     return 1
    if check_win(HUMAN):  return -1
    if board_is_full():   return 0

    if is_maximizing:                     # AI's turn
        best = -infinity
        for each empty cell:
            simulate AI move
            best = max(best, minimax(board, depth+1, False, alpha, beta))
            undo move
        return best
    else:                                  # Human's turn
        best = +infinity
        for each empty cell:
            simulate human move
            best = min(best, minimax(board, depth+1, True, alpha, beta))
            undo move
        return best
```

Because Tic-Tac-Toe has at most **9! = 362,880** possible move sequences, this brute-force approach is entirely feasible to compute in real time.

---

## ✂️ Alpha-Beta Pruning Explanation

> **Beginner-friendly summary:** Alpha-Beta Pruning is Minimax with a memory of "the best score I've already found elsewhere." If a branch can mathematically never beat what's already guaranteed, there's no point finishing the calculation — so the algorithm abandons it early.

Two values are tracked while traversing the tree:

- **Alpha (α)** — the best score the **maximizer (AI)** can guarantee so far.
- **Beta (β)** — the best score the **minimizer (human)** can guarantee so far.

**The pruning rule:** whenever `α >= β`, the current branch is cut off immediately — no further exploration is needed, because a rational opponent would never let the game reach this point anyway.

```python
alpha = max(alpha, best_score)
if alpha >= beta:
    return best_score   # 🔪 Prune remaining branches — they cannot change the result
```

**Why this matters:** Alpha-Beta Pruning produces the **exact same decisions** as plain Minimax — it changes *how fast* the answer is found, never *what* the answer is. See real measured numbers in [Performance Analysis](#-performance-analysis).

---

## 🎲 Game Theory Concepts

| Concept | How It Applies to Tic-Tac-Toe |
|---|---|
| **Zero-Sum Game** | One player's gain is exactly the other's loss — the AI's `+1` is the human's `-1` |
| **Perfect Information** | Both players can always see the entire board; there's no hidden state |
| **Deterministic Game** | No randomness or dice rolls involved — every outcome follows directly from the moves made |
| **Finite Game Tree** | The game must end within 9 moves, guaranteeing the search always terminates |
| **Solved Game** | Tic-Tac-Toe has been mathematically proven to always end in a draw with two perfect players — exactly what [Test 6 in our test suite](#-performance-analysis) demonstrates |
| **Minimax Theorem** | In zero-sum games, there exists an optimal strategy where each player minimizes their maximum possible loss |

---

## 🏗️ Project Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                     Pygame Event Loop                    │
│   (mouse clicks, key presses, render every frame)        │
└───────────────────────────┬───────────────────────────────┘
                            │
            ┌───────────────┼────────────────┐
            ▼                                 ▼
 ┌────────────────────┐           ┌────────────────────────┐
 │   Human Move        │           │   AI Move Engine        │
 │  mark_square(...)    │           │  best_ai_move(level)    │
 └──────────┬───────────┘           └────────────┬─────────────┘
            │                                     │
            ▼                                     ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                    Game State (NumPy board)                  │
 │     check_win() · is_board_full() · get_winning_line()       │
 └───────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Minimax + Alpha-Beta   │
                 │   (recursive search)     │
                 └────────────┬──────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Rendering / Scoreboard  │
                 │ draw_figures(), draw_     │
                 │ winning_line(), top bar   │
                 └─────────────────────────┘
```

---

## 📂 Folder Structure

```
tic-tac-toe-ai-minimax/
│
├── tic_tac_toe_ai.py      # 🎮 Complete game: GUI, rules, AI engine
├── requirements.txt        # 📦 Pygame + NumPy dependencies
├── README.md                # 📘 You are here
```

> This project is intentionally implemented as a single, well-organized file for clarity and portability — every function is documented and grouped by responsibility (drawing, game state, AI engine, main loop)

---

## 📋 Requirements

| Requirement | Minimum Version |
|---|---|
| Python | 3.8+ |
| Pygame | 2.5.0+ |
| NumPy | 1.24.0+ |

`requirements.txt`:
```
pygame>=2.5.0
numpy>=1.24.0
```

---

## ▶️ How to Run

```bash
python tic_tac_toe_ai.py
```

**Controls:**

| Input | Action |
|---|---|
| 🖱️ Left Click | Place your mark on an empty square |
| `1` | Set difficulty to **Easy** |
| `2` | Set difficulty to **Medium** |
| `3` | Set difficulty to **Hard** (unbeatable) |
| `R` | Restart the current round (scoreboard is preserved) |

---

## 🕹️ Gameplay Walkthrough

1. Launch the game — the board appears with a scoreboard reading `You: 0  AI: 0  Draws: 0` and `Difficulty: Hard`.
2. Optionally press `1` or `2` to make the AI easier before you start.
3. Click any empty square to place your **O**.
4. The AI immediately responds with its **X** in the same frame.
5. After each move, the game checks all 8 winning lines and the board-full condition.
6. When the round ends, the winning line is drawn in **green** (you win), **red** (AI wins), or the board turns **gray** (draw) — and the scoreboard updates.
7. Press `R` at any time to start a fresh round without closing the game.

---

## 🔍 Example AI Decision Process

Consider this board state, where the AI (`X`) must move:

```
 O | O | .
-----------
 X | . | .
-----------
 . | . | .
```

The human has two in a row on the top row with one empty square remaining (top-right). Walking through Minimax:

1. The AI evaluates **every** empty square, including the top-right corner.
2. If the AI does **not** play top-right, Minimax simulates the human's next move filling that square → result: human wins → score `-1` for that branch.
3. If the AI **does** play top-right, that branch can no longer result in a human win on this line → Minimax continues exploring deeper, ultimately returning a `0` (draw) or better.
4. Comparing all 9 possible branches, the move **top-right** is the only one that avoids an immediate `-1` outcome.
5. The AI plays top-right — a textbook defensive block, discovered automatically with no hardcoded "if human has two in a row, block it" rule. The behavior **emerges naturally** from exhaustively scoring every future.

This is exactly what our automated test suite verifies (see [Performance Analysis](#-performance-analysis) below).

---

## 📊 Performance Analysis

Real benchmark results, measured by counting recursive calls when the AI decides its **very first move from an empty board** — the worst-case, most expensive search in the entire game:

| Approach | Nodes Evaluated | Time Taken | Result |
|---|---|---|---|
| Plain Minimax (no pruning) | **549,946** | ~7.7 seconds | Optimal move found |
| Minimax + Alpha-Beta Pruning | **18,297** | ~0.27 seconds | **Identical** optimal move found |
| **Improvement** | **96.7% fewer nodes explored** | **~28x faster** | Same correctness guarantee |

**Key takeaways:**

- Alpha-Beta Pruning never changes *what* the AI decides — only *how much work* it takes to get there. Both approaches choose the exact same move in every test.
- A full plain-Minimax search of Tic-Tac-Toe (549,946 nodes) is still trivial for a modern CPU, but the difference becomes dramatically more important in larger games (Connect Four, Chess, Go), where pruning is the difference between *feasible* and *computationally impossible*.
- Automated self-play testing (Hard AI vs. an optimal-playing simulated opponent) was run to verify the **unbeatability guarantee**: across exhaustive simulation, two perfect players always reach a **draw**, exactly as game theory predicts for Tic-Tac-Toe.

---

## 🚀 Future Improvements

- 🌳 Add **move ordering and transposition tables** to further speed up search (most valuable for larger board variants)
- 🧩 Generalize the engine to **N×N boards** and **Connect Four**-style win conditions
- 🌐 Add an **online multiplayer mode** using sockets
- 🔊 Add sound effects and simple win/loss animations
- 📱 Port the GUI to a web-based version using Pygame-to-WASM or a JS/Canvas rewrite
- 📈 Add a persistent leaderboard saved to a local file or database
- 🧪 Expand the automated test suite with `pytest` and CI integration (GitHub Actions)

---

## 🎓 Learning Outcomes

By completing this project, you will be able to:

- Implement a **recursive game-tree search algorithm** (Minimax) from scratch
- Understand and apply **Alpha-Beta Pruning** as a real optimization technique
- Translate **game theory concepts** (zero-sum games, perfect information) into working code
- Build an **interactive GUI application** with Pygame, including event handling and rendering
- Represent and manipulate game state efficiently using **NumPy arrays**
- Design and run **automated tests** to verify algorithmic correctness (including a self-play proof of unbeatability)
- Structure a small project for **professional, recruiter-ready GitHub presentation**

---

## 🌍 Applications

The exact same Minimax + Alpha-Beta approach used here scales conceptually to:

- ♟️ **Chess and Checkers engines** (with deeper search and heuristic evaluation functions)
- 🎮 **Turn-based strategy game AI** (Connect Four, Othello, board games)
- 🧮 **Automated decision-making systems** under adversarial or competitive conditions
- 📈 **Auction and negotiation bots** modeled as zero-sum or general-sum games
- 🤖 **Educational tools** for teaching recursion, search, and game theory in CS curricula

---

## ✅ Advantages

- **Provably optimal** — the AI's Hard mode cannot lose; the worst outcome is a draw
- **Fully explainable** — every decision can be traced through a deterministic search tree, unlike black-box ML models
- **No training data or GPU required** — runs instantly on any machine with Python
- **Difficulty scaling** — Easy/Medium modes keep the game enjoyable for beginners and casual players
- **Lightweight dependencies** — only Pygame and NumPy, no heavy ML frameworks

---

## ⚠️ Limitations

- Minimax's brute-force approach **does not scale** to larger games (Chess, Go) without heuristic evaluation functions and much deeper optimizations
- The current implementation **recomputes the full search tree on every AI move** rather than caching/reusing previous computations (no transposition table)
- The GUI is intentionally minimal — no animations, sound, or networked multiplayer
- Medium difficulty's "50% random" model is a simple heuristic, not a calibrated skill curve
---

<div align="center">
