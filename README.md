# 🧠 Wordle Solver

A Python-based utility for filtering and suggesting valid 5-letter words based on Wordle-style constraints. This tool helps you narrow down possible guesses using green (correct), yellow (misplaced), and gray (excluded) letters.

---

## 📦 Project Structure

wordle-solver/\
├── database/\
│ ├── database.db # SQLite DB with a 'words' table\
│ ├── word_db.py # Core logic for querying word options\
│ └── words_alpha.csv # Word dictionary to import to db\
├── wordle_solver.py # Main logic for processing guesses\
├── main.py # Example usage\
└── README.md # You're here!

---

## 🚀 Features

- ✅ **Green letters**: Correct letters in the correct position
- 🟨 **Yellow letters**: Correct letters in the wrong position
- ⬛ **Gray letters**: Letters not in the word at all
- 🔍 **Dynamic SQL filtering**: Efficiently queries a word list using constraints
- 🧪 **Testable and modular**: Easily extendable for other word-based games

---

## 🛠️ Usage

```python
from database.word_db import get_word_options

grn = ['_', 'I', '_', '_', '_']         # Green letters (correct position)
yel = [[], [], ['G'], [], ['T']]        # Yellow letters (wrong position)
gry = ['A', 'S', 'L', 'E', 'D', 'Y']     # Gray letters (excluded)

options = get_word_options(grn, yel, gry)
guesses = [word for word in options if len(word) == 5]
print(guesses)
```
## 🧠 How It Works
The SQL query is dynamically built to reflect the constraints:

LIKE '_I___': Green letters are fixed in position
SUBSTR(word, i+1, 1) != 'x': Yellow letters must not be in their original position
word LIKE '%x%': Yellow letters must be present somewhere
word NOT LIKE '%x%': Gray letters must be excluded entirely

## 🗃️ Database Requirements
Your SQLite database (database.db) should contain a table named words with a single column:


Populate it with lowercase 5-letter words (e.g., from dwyl/english-words).

## 📌 Example

Generates SQL like:

```sql
SELECT * FROM words
WHERE word LIKE '_i___'
  AND SUBSTR(word, 3, 1) != 'g'
  AND word LIKE '%g%'
  AND SUBSTR(word, 5, 1) != 't'
  AND word LIKE '%t%'
  AND word NOT LIKE '%a%'
  AND word NOT LIKE '%s%'
  ...
```

## 🙌 Contributions
Feel free to fork, open issues, or submit pull requests. Feedback and improvements are welcome!

Would you like me to create this file and push it to your repo, or would you prefer to copy and paste it yourself?

!License: MIT