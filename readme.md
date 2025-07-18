🧠 Word Filter Tool for Wordle-Like Games
This project provides a Python-based utility to query a SQLite word database using constraints inspired by Wordle-style gameplay. It supports:

✅ Green letters (correct position)

🟡 Yellow letters (wrong position but present)

⬛ Gray letters (excluded entirely)

📦 Project Structure
project/
├── database/
│   └── database.db         # SQLite DB with a 'words' table
├── database/
│   └── word_db.py          # Core logic for querying word options
├── main.py                 # Example usage
└── README.md               # You're here!
🔧 Usage
python
from database.word_db import get_word_options

grn = ['_', 'I', '_', '_', '_']       # Green letters (correct position)
yel = ['_', '_', 'G', '_', 'T']       # Yellow letters (wrong position)
gry = ['A', 'S', 'L', 'E', 'D', 'Y']  # Gray letters (excluded)

options = get_word_options(grn, yel, gry)
guesses = [word for word in options if len(word) == 5]

print(guesses)
🧠 Logic Behind the Query
The SQL query is dynamically built to reflect the constraints:

LIKE '_i___': Green letters are fixed in position

SUBSTR(word, i+1, 1) != 'x': Yellow letters must not be in their original position

LIKE '%x%': Yellow letters must be present somewhere

NOT LIKE '%x%': Gray letters must be excluded entirely

🗃️ Database Requirements
Your SQLite database (database.db) should contain a table named words with a single column:

sql
CREATE TABLE words (
    word TEXT
);
Populate it with lowercase words (e.g., from dwyl/english-words).

🧪 Example Query
For:

python
grn = ['_', 'I', '_', '_', '_']
yel = ['_', '_', 'G', '_', 'T']
gry = ['A', 'S', 'L', 'E', 'D', 'Y']
The generated SQL will look like:

sql
SELECT * FROM words
WHERE word LIKE '_i___'
  AND SUBSTR(word, 3, 1) != 'g'
  AND word LIKE '%g%'
  AND SUBSTR(word, 5, 1) != 't'
  AND word LIKE '%t%'
  AND word NOT LIKE '%a%'
  AND word NOT LIKE '%s%'
  AND word NOT LIKE '%l%'
  AND word NOT LIKE '%e%'
  AND word NOT LIKE '%d%'
  AND word NOT LIKE '%y%';