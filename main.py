#POMODORO APP
"""
POMODORO TIMER
Work -> Break -> Work
With clear phases and sound alerts.
"""

import time


def format_time(remaining):
    rem_h = remaining // 3600
    rem_min = (remaining % 3600) // 60
    rem_sec = remaining % 60
    return rem_h, rem_min, rem_sec

def timer_run(minutes: int):
    total_sec = minutes * 60
    for remaining in range(total_sec, -1, -1):
        rem_h, rem_min, rem_sec = format_time(remaining)
        print(f"\r{rem_h}H: {rem_min}M: {rem_sec}S", end="", flush=True)
        time.sleep(0.1)

timer_run(90)