import time
from tkinter import *
from tkinter import messagebox

# Setting up the Tkinter window
root = Tk()
root.title('Speed Typer')
root.geometry("790x790")
root.title("Speed Typer Pro")

# Empty list to be populated with characters from text file
char_list = []
# Empty string to receive char_list items as a string
char_text = ''
# Empty list to receive keystrokes
key_list = []

# Opening and reading text file and adding characters to list.
# Could be upgraded to select a random text file from a number of saved options.
text_file = open('Text_Files/typing_text1.txt', 'r')
text = text_file.read()
for char in text:
    char_list.append(char)
char_text = char_text.join(char_list)

# Declaration of timer variables
second = StringVar()
# setting timer start value as 60secs
second.set("60")


# Wrapper to only run a function once even if it's called multiple times
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


# Applying wrapper so that timer is started on first keystroke but not on subsequent inputs
@run_once
# 60-second countdown timer
def start_timer():
    temp = int(second.get())
    while temp > -1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)
        # using format () method to store the value up to two decimal places
        second.set("{0:2d}".format(secs))
        # updating the GUI window after decrementing the temp value every time
        timer_box.update()
        time.sleep(1)
        # when temp value = 0; then a messagebox pop's up with a message:"Time's up"
        if temp == 0:
            messagebox.showinfo(f"Your results!", f"Well done, you typed {len(key_list)} characters in one minute")
        # after every one sec the value of temp will be decremented by one
        temp -= 1


# Stores key presses in a list and removes last item if 'delete' is pressed
# First key press starts timer
# Calls function to compare key inputs to char_list
def key_press(event):
    key = event.char
    output_text = ''
    if key == '':
        key_list.pop()
    else:
        key_list.append(key)
    output_text = output_text.join(key_list)
    output_box.config(text=output_text)
    list_compare()
    start_timer()


# Compares key inputs to char_list to see if word has been typed correctly.
# If correct turns text green, if incorrect turns text red.
def list_compare():
    chars_typed = len(key_list)
    if key_list == char_list[0:chars_typed]:
        output_box.config(fg='green')
    else:
        output_box.config(fg='red')


# Widgets
timer_box = Label(root, width=3, font=("Arial", 40, ""), fg='yellow', bg='black',
                  textvariable=second)
text_box = Label(text=char_text, font=("Arial", 22, ""), height=10, width=60, bg='white', fg='black', wraplength=600)
typing_box_label = Label(text='Type here:', font=("Arial", 22, ""), anchor='center')
typing_box = Entry(width=40, font=("Arial", 22, ""))
typing_box.bind('<Key>', key_press)
output_box = Label(text='', font=("Arial", 22, ""), width=60, wraplength=600)
output_box.bind('<Key>', key_press)

# Grid positions
timer_box.grid(row=0, column=0, pady=20)
text_box.grid(row=1, column=0, columnspan=1)
typing_box_label.grid(row=2, column=0, sticky=NW)
typing_box.grid(row=2, column=0)
output_box.grid(row=4, column=0, columnspan=1)

root.mainloop()
