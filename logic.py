from datetime import datetime

LOG_FILE = "logs.txt"

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
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line:
                    line.strip()
                    list_lines.append(line)
        return reversed(list_lines)
    

    
