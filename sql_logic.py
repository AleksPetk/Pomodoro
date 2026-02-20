import sqlite3

class Pomodoro_sql:
    def __init__(self):
        self.filename = "pomodoro.db"
        self.table_history = "history"
        
    def connect(self):
        self.conn = sqlite3.connect(self.filename)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def folder_history_ensure(self):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_history} (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         date_time TEXT,
                         work_minutes INTEGER,
                         break_minutes INTEGER,
                         rounds INTEGER,
                         complete_rounds INTEGER DEFAULT 0)""")
    
    def on_start(self, date_time, work_minutes, break_minutes, rounds):
        self.cur.execute(f"INSERT INTO {self.table_history} (date_time, work_minutes, break_minutes, rounds) VALUES (?, ?, ?, ?)",
                         (date_time, work_minutes, break_minutes, rounds))
        
    def comp_rounds(self, start_time):
        self.cur.execute(f"UPDATE {self.table_history} SET complete_rounds = complete_rounds + 1 WHERE date_time = ?", (
            start_time,))
        
    def return_row(self):
        self.cur.execute(f"SELECT * FROM {self.table_history} ORDER BY id DESC LIMIT 20")
        rows = self.cur.fetchall()
        return rows
    
    def save_conn(self):
        self.conn.commit()