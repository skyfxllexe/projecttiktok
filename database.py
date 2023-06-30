
import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS accounts(
   nickname TEXT,
   time INTEGER,
   scheme TEXT,
   content_type TEXT,
   proxy TEXT,
   condition TEXT,
   cookie TEXT,
   is_alive BOOL,
   login TEXT,
   password TEXT,
   user_agent TEXT
);
''')