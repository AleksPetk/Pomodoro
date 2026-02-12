import time
from logic import Logic

"""
POMODORO TIMER
Work -> Break -> Work
With clear phases and sound alerts.
"""
# Fast secs!

class App:
    def __init__(self):
        pass

    def timer_run(self, minutes: int, round, phrase):
        total_sec = minutes * 60
        for remaining in range(total_sec, -1, -1):
            rem_h, rem_min, rem_sec = Logic.format_time(remaining)
            print(f"\r{round}. {phrase} | {rem_h}H: {rem_min}M: {rem_sec}S", end="", flush=True)
            time.sleep(0.0001)
        print(" Finished")

    def menu(self):
        menu_list = ["Set timer", "Exit"]
        for e, opt in enumerate(menu_list, 1):
            print(f"{e}. {opt}")

        return len(menu_list)

    def user_int(self, max_v):
        while True:
            try:
                user_opt = int(input("Option: "))
                if 1 <= user_opt <= max_v:
                    return user_opt
                else: 
                    print("Not such a option!")
            except ValueError:
                print("Numbers only")

    def set_input(self, phrase):
        while True:
            try:
                user_opt = int(input(f"{phrase}: "))
                if 1 <= user_opt:
                    return user_opt
                else: 
                    print("Can't be less than 1!")
            except ValueError:
                print("Numbers only")

    def timer_set(self):
        get_work = self.set_input("Work Time")
        get_break = self.set_input("Break")
        get_rounds = self.set_input("Rounds")
        for round in range(1,get_rounds+1):
            self.timer_run(get_work, round, "Work")
            self.timer_run(get_break, round, "Break")





    def navigator(self,user_in):
        match user_in:
            case 1:
                self.timer_set()
            case 2:
                exit()

    def mainloop(self):
        while True:
            print("\nPomodoro Timer\n")
            max_v = self.menu()
            user_in = self.user_int(max_v)
            self.navigator(user_in)

    def run(self):
        self.mainloop()