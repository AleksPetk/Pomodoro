#POMODORO APP
"""
POMODORO TIMER
Work -> Break -> Work
With clear phases and sound alerts.
"""
# Fast secs!
import time


def format_time(remaining):
    rem_h = remaining // 3600
    rem_min = (remaining % 3600) // 60
    rem_sec = remaining % 60
    return rem_h, rem_min, rem_sec

def timer_run(minutes: int, round, phrase):
    total_sec = minutes * 60
    for remaining in range(total_sec, -1, -1):
        rem_h, rem_min, rem_sec = format_time(remaining)
        print(f"\r{round}. {phrase} | {rem_h}H: {rem_min}M: {rem_sec}S", end="", flush=True)
        time.sleep(0.0001)
    print(" Finished")

def menu():
    menu_list = ["Set timer", "Exit"]
    for e, opt in enumerate(menu_list, 1):
        print(f"{e}. {opt}")

    return len(menu_list)

def user_int(max_v):
    while True:
        try:
            user_opt = int(input("Option: "))
            if 1 <= user_opt <= max_v:
                return user_opt
            else: 
                print("Not such a option!")
        except ValueError:
            print("Numbers only")

def set_input(phrase):
    while True:
        try:
            user_opt = int(input(f"{phrase}: "))
            if 1 <= user_opt:
                return user_opt
            else: 
                print("Can't be less than 1!")
        except ValueError:
            print("Numbers only")

def timer_set():
    get_work = set_input("Work Time")
    get_break = set_input("Break")
    get_rounds = set_input("Rounds")
    for round in range(1,get_rounds+1):
        timer_run(get_work, round, "Work")
        timer_run(get_break, round, "Break")





def navigator(user_in):
    match user_in:
        case 1:
            timer_set()
        case 2:
            exit()

def mainloop():
    while True:
        print("\nPomodoro Timer\n")
        max_v = menu()
        user_in = user_int(max_v)
        navigator(user_in)

mainloop()