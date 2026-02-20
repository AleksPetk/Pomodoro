from datetime import datetime
from sql_logic import Pomodoro_sql
LOG_FILE = "logs.txt"

pomo_logic = Pomodoro_sql()

class Logic:


    def format_time(remaining):
        rem_h = remaining // 3600
        rem_min = (remaining % 3600) // 60
        rem_sec = remaining % 60
        return rem_h, rem_min, rem_sec
    
    def logs_save(log_text):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(time_now + log_text + "\n")

    def logs_read():
        list_lines = []
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    if line:
                        line = line.strip()
                        list_lines.append(line)
        except FileNotFoundError:
            list_lines.append("No logs yet!")
        return reversed(list_lines)
    
    def sql_onstart(work_min, break_min, rounds):
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pomo_logic.on_start(start_time, work_min, break_min, rounds)
        pomo_logic.save_conn()
        return start_time

    def sql_ensuref():
        pomo_logic.connect()
        pomo_logic.folder_history_ensure()

    def update_rounds(start_time):
        pomo_logic.comp_rounds(start_time)
        pomo_logic.save_conn()

    def close_sql():
        pomo_logic.close()

    def view_sql():
        rows = pomo_logic.return_row()
        history_list = []
        if not rows:
            text = "No SQL history yet!"
            history_list.append(text)
            return history_list
        for row in rows:
            text_list = []
            text = f"ID: {row[0]} TIME: {row[1]}"
            text_list.append(text)
            text1 = f"Work: {row[2]} min Break: {row[3]} min"
            text_list.append(text1)
            text2 = f"Rounds Set: {row[4]} Rounds Done: {row[5]}"
            text_list.append(text2)

            history_list.append(text_list)
        return history_list
        

    

    
