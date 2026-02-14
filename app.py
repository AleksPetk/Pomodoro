from logic import Logic
from ui_pages import HEADER, Main, CONTENT_COLOR, HEADER_COLOR, Set_T, Running, Logs_view
import tkinter as tk


# Fast secs!

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Pomodore")
        self.root.resizable(False, False)

        self.sections = {}
        self.sections["header"] = tk.Frame(self.root, height=100,width=600, bg=HEADER_COLOR)
        self.sections["content"] = tk.Frame(self.root, height=500, width=600, bg=CONTENT_COLOR)
        for section in self.sections.values():
            section.pack()
            section.propagate(False)

        header = HEADER(self.sections["header"])
        header.pack()

        self.content = {}
        self.content["main"] = Main(self.sections["content"], self)
        self.content["entry"] = Set_T(self.sections["content"], self)
        self.content["run"] = Running(self.sections["content"], self)
        self.content["logs"] = Logs_view(self.sections["content"], self)

        for page in self.content.values():
            page.place(x=0, y=0)

        self.show_page(self.content["main"])

    def logs(self):
        self.content['logs'].logs_list.delete(0, tk.END)
        list_logs = Logic.logs_read()
        for e, log in enumerate(list_logs, 1):
            self.content['logs'].logs_list.insert(tk.END, f"{e}. {log}")
        self.show_page(self.content['logs'])

    def selected(self, event = None):
        self.work_min = self.content['entry'].entry_work.get()
        self.break_min= self.content['entry'].entry_break.get()
        self.rounds= self.content['entry'].entry_round.get()
        if self.work_min.isdigit() and self.rounds.isdigit() and self.break_min.isdigit() :
            self.content['entry'].label_about.config(text = 'Timer can be set!', bg = "lightgreen")
            self.content['entry'].start_b.config(state = "normal")
        else:
            self.content['entry'].label_about.config(text = 'You need to set first', bg = CONTENT_COLOR)
            self.content['entry'].start_b.config(state = "disabled")


    def start_pressed(self):
        self.content['entry'].start_b.config(state = "disabled")
        self.content['entry'].entry_work.delete(0, tk.END)
        self.content['entry'].entry_break.delete(0, tk.END)
        self.content['entry'].entry_round.delete(0, tk.END)
        self.content['entry'].label_about.config(text = 'Set Timer', bg = CONTENT_COLOR)
        
        work_min = int(self.work_min)
        rounds = int(self.rounds)
        break_min = int(self.break_min)
        
        self.show_page(self.content['run'])

        self.timer_set(work_min, rounds, break_min)

    def show_page(self,page):
        page.tkraise()

    def run(self):
        Logic.logs_save(" App opened ")
        self.root.mainloop()




    def timer_set(self, work_min: int, rounds: int, break_min: int):
        self.work_sec = work_min * 60
        self.break_sec = break_min * 60
        self.total_rounds = rounds

        self.round_num = 1
        self.phase = "Work"          
        self.remaining = self.work_sec

        self.running = True
        self.pause = False
        self.after_id = None

        self._tick()

    def _tick(self):
        if not self.running or self.pause:
            return
        
        rem_h, rem_min, rem_sec = Logic.format_time(self.remaining)
        self.content['run'].timer.config(
            text=f"{self.round_num}. {self.phase} | {rem_h}H: {rem_min}M: {rem_sec}S"
        )

        
        if self.remaining <= 0:
            self._next_phase_or_round()
            return

       
        self.remaining -= 1
        self.after_id = self.root.after(1, self._tick)

    def _next_phase_or_round(self):
        if self.phase == "Work":
            self.phase = "Break"
            self.remaining = self.break_sec
        else:
            if self.round_num >= self.total_rounds:
                self.content['run'].timer.config(text="Finished ✅")
                self.root.after(1500,lambda: self.show_page(self.content["entry"]))
                self.running = False
                self.after_id = None
    
                return

            self.round_num += 1
            self.phase = "Work"
            self.remaining = self.work_sec
        self.after_id = self.root.after(0, self._tick)

    def stop(self):
        self.running = False
        self.pause = False
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None
            self.content['run'].timer.config(text="Stopped ⏹")
            self.root.after(1500,lambda: self.show_page(self.content["entry"]) )
            self.content["run"].pause_resume.config(text = "Pause")

    def resume_pause(self):
        if not self.pause:
            self.content["run"].pause_resume.config(text = "Resume")
            self.pause = True
        elif self.pause:
            self.content["run"].pause_resume.config(text = "Pause")
            if not self.running:
                return
            if not self.pause:
                return
            self.pause = False
            self.after_id = self.root.after(0, self._tick)

