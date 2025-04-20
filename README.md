# 🧠 Chess Engine Bot

A basic but growing chess engine written in Python, using `python-chess`, `minimax`, and a handcrafted evaluation function. It supports classic play against a human, includes opening book support, and is gradually evolving into a real menace 😈.

---

## ♟ Features

- Minimax algorithm with alpha-beta pruning  
- Quiescence search for deeper tactical stability  
- Static evaluation: material + mobility + castling rights  
- Move ordering: prioritizes captures first  
- Supports pawn promotions  
- Reads ECO openings from `eco.json`  
- Pure console interface (no GUI)

---

## 💠 Requirements

- Python 3.8+  
- [python-chess](https://pypi.org/project/python-chess/)

Install with:

```
pip install python-chess
```

---

## ▶️ How to Play

Just run:

```
python bot.py
```

You play as White. Type your moves in UCI format, like:

```
e2e4
e7e8q  ← for promotions
```

The bot plays back as Black. The game continues until checkmate or draw. At the end, it shows the result and final evaluation.

---

## 📁 Files

| File        | Description                              |
|-------------|------------------------------------------|
| `bot.py`    | The main engine script                   |
| `eco.json`  | Opening book used in early positions     |
| `README.md` | You're reading it                        |

---

## 🚧 Roadmap

- [ ] Add iterative deepening with time control  
- [ ] Detect tactical threats (forks, pins)  
- [ ] Endgame knowledge (passed pawns, active king)  
- [ ] PGN output
- [ ] Add option to play as Black or White
- [ ] Add time control settings (10min, 5min, 1min) with adaptive depth

---

## 📸 Screenshot


## ✨ Credits

Built with ❤️ and way too many sleepless nights.

By MrSayyrenN.

