import os
import sqlite3
def get_word_options(grn, yel, gry):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = convert_to_sql(grn, yel, gry)
    cursor.execute(sql)
    options = [row[0] for row in cursor.fetchall()]
    conn.close()
    return options

def convert_to_sql(grn, yel, gry):
    green = ''.join(grn).lower()
    sql = f"SELECT * FROM words WHERE word LIKE '{green}'"
    n = len(grn)
    for i in range(n):
        if grn[i] == '_':
            if yel[i] != '_':
                sql += f" AND SUBSTR(word, {i+1}, 1) != '{yel[i].lower()}'"
        if yel[i] != '_':
            sql += f" AND word LIKE '%{yel[i].lower()}%'"
    for g in gry:
        sql += f" AND word NOT LIKE '%{g.lower()}%'"
    return sql