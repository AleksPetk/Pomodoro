import tkinter as tk

HEADER_COLOR = "#08FFB5"
CONTENT_COLOR = "#089CFF"
LABEL_FONT = ("Arial", 30)
BUTTONS_FONT = ("Arial", 30)
SMALL_LABELS = ("Arial", 20)



class HEADER(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        header_frame = tk.Frame(self, height=100, width=600, bg = HEADER_COLOR)
        header_frame.pack(fill="both")
        header_frame.pack_propagate(False)
        tk.Label(header_frame,text="Pomodoro App", bg=HEADER_COLOR, font=LABEL_FONT, relief= "groove", fg=CONTENT_COLOR).pack(pady=20)

class Main(tk.Frame):
    def __init__(self, parent, controler):
        super().__init__(parent)
        frame = tk.Frame(self,height=500, width=600, bg=CONTENT_COLOR )
        frame.pack(fill="both")
        frame.pack_propagate(False)

        tk.Button(frame, text="Set Timer", font=BUTTONS_FONT, command=lambda: controler.show_page(controler.content["entry"])).pack(pady=50)
        tk.Button(frame, text="Exit", font=BUTTONS_FONT, command=controler.root.destroy).pack(pady=50)

class Set_T(tk.Frame):
    def __init__(self, parent, controler):
        super().__init__(parent)
        frame = tk.Frame(self,height=500, width=600, bg=CONTENT_COLOR )
        frame.pack(fill="both")
        frame.pack_propagate(False)


        entryframe = tk.Frame(frame, height=200, width=500, bg =CONTENT_COLOR, highlightthickness=3, highlightbackground="black")
        entryframe.pack(pady=10)
        entryframe.grid_propagate(False)
        entryframe.rowconfigure(0, weight=1)
        entryframe.rowconfigure(1, weight=1)
        entryframe.rowconfigure(2, weight=1)
        entryframe.columnconfigure(0, weight=1)
        entryframe.columnconfigure(1, weight=1)
        
        
        tk.Label(entryframe, text="Work time (min)", font=SMALL_LABELS, bg = CONTENT_COLOR).grid(row=0, column=0)
        tk.Label(entryframe, text="Break time (min)", font=SMALL_LABELS, bg = CONTENT_COLOR).grid(row=1, column=0)
        tk.Label(entryframe, text="Rounds repeat", font=SMALL_LABELS, bg = CONTENT_COLOR).grid(row=2, column=0)
        self.entry_work = tk.Entry(entryframe, font=SMALL_LABELS, bg = CONTENT_COLOR, width=10)
        self.entry_work.grid(row=0, column=1)
        self.entry_work.bind("<KeyRelease>", controler.selected)
        self.entry_break = tk.Entry(entryframe, font=SMALL_LABELS, bg = CONTENT_COLOR, width=10)
        self.entry_break.grid(row=1, column=1)
        self.entry_break.bind("<KeyRelease>", controler.selected)
        self.entry_round = tk.Entry(entryframe, font=SMALL_LABELS, bg = CONTENT_COLOR, width=10)
        self.entry_round.grid(row=2, column=1)
        self.entry_round.bind("<KeyRelease>", controler.selected)

        self.label_about = tk.Label(frame, text="Set Timer", font=BUTTONS_FONT, bg= CONTENT_COLOR)
        self.label_about.pack(pady=10)

        self.start_b = tk.Button(frame, text="Start", font=BUTTONS_FONT, state="disabled", command=controler.start_pressed)
        self.start_b.pack(pady=10)
        tk.Button(frame, text="Back", font=BUTTONS_FONT, command=lambda: controler.show_page(controler.content["main"])).pack(pady=10)



class Running(tk.Frame):
    def __init__(self, parent, controler):
        super().__init__(parent)
        frame = tk.Frame(self,height=500, width=600, bg=CONTENT_COLOR )
        frame.pack(fill="both")
        frame.pack_propagate(False)

        self.timer = tk.Label(frame, text="", font=LABEL_FONT)
        self.timer.pack(pady=30)

        self.stop = tk.Button(frame, text="Stop", font=BUTTONS_FONT, state="normal", command=controler.stop)
        self.stop.pack(pady=10)
        self.pause_resume = tk.Button(frame, text="Pause", font=BUTTONS_FONT, command=controler.resume_pause)
        self.pause_resume.pack(pady=10)

    

