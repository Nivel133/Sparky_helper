import sqlite3 as sq
from core.utils.utils import parser_of_data_hw

async def db_connect() -> None:
    global db, cur

    db = sq.connect('core/data/homework.db')
    cur = db.cursor()

    cur.execute('''
CREATE TABLE IF NOT EXISTS Homework (
id INTEGER PRIMARY KEY,
user_id INTEGER NOT NULL,
homework TEXT
)
''')

    db.commit()



async def create_hw(userid, homework):
    cur.execute('INSERT INTO Homework (user_id, homework) VALUES (?, ?)',
                   (userid, homework))
    db.commit()


async def get_all_hw(userid):
    cur.execute(f'SELECT homework FROM Homework WHERE user_id = {userid}')
    return parser_of_data_hw(cur.fetchall())





