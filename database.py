import sqlite3


def create_database():
    conn = sqlite3.connect('employee_log.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            action TEXT NOT NULL,
            date TEXT NOT NULL,
            rating INTEGER NOT NULL,
            note TEXT  -- Поле для примечания
            );
        ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
