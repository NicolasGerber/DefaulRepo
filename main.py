from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="FOCUS",fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        timer_label.config(text="BREAK",fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="BREAK",fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count < 0:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW, highlightthickness=0)



canvas = Canvas(width=200,height=224,bg=YELLOW)
tomate = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomate,)
timer_text = canvas.create_text(103,130,text="00:00", fill="white",font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2,column=2)

timer_label = Label(text="TIMER",
                    fg=GREEN,
                    highlightthickness=0,
                    font=(FONT_NAME,36,"bold"),
                    bg=YELLOW)
timer_label.grid(row=0,column=2)


start_B = Button(text="Start",
                 command=start_timer)
start_B.grid(row=3,column=1)


reset_B = Button(text="Reset",
                 command=reset_timer)
reset_B.grid(row=3,column=3)


checkmark = Label(text="",
                  fg=GREEN,
                  highlightthickness=0,
                  bg=YELLOW,
                  font=(FONT_NAME,33,"bold"))
checkmark.grid(row=4,column=2)




window.mainloop()