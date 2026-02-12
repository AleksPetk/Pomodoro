

class Logic:


    def format_time(remaining):
        rem_h = remaining // 3600
        rem_min = (remaining % 3600) // 60
        rem_sec = remaining % 60
        return rem_h, rem_min, rem_sec
    
    