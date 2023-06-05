from tkinter import *
import math
import time
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
def reset():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Long break")
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short break")
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work timer")


        
    
    
    
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else: 
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)




title_label = Label(bg=GREEN)
title_label.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=YELLOW)
title_label.pack()

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomate_img)
timer_text = canvas.create_text(106, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 33, "bold"))
canvas.pack()



start_button = Button(text="Start", command=start_timer)
start_button.pack(side=LEFT)

#check_label = Label(text="✔",fg=RED,bg=GREEN, font=(FONT_NAME,10,"bold"))
#check_label.pack(side=BOTTOM)

reset_button = Button(text="Reset", command=reset)
reset_button.pack(side=RIGHT)






















window.mainloop()