from tkinter import *
from tkinter import messagebox

current_player = "X"

game_count = 1


def on_btn_pressed(button):
    global current_player, game_count
    if button["text"] == "":
        button["text"] = current_player
        game_count = game_count + 1
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    check_winner()


def reset_game():
    global current_player, game_count

    current_player = "X"
    game_count = 1
    button11["text"] = button12["text"] = button13["text"] = button21["text"] = button22["text"] = button23["text"] = \
        button31["text"] = button32["text"] = button33["text"] = ""

    button11["bg"] = button12["bg"] = button13["bg"] = button21["bg"] = button22["bg"] = button23["bg"] = \
        button31["bg"] = button32["bg"] = button33["bg"] = "#aaaaaa"


def check_winner():
    # X Conditions
    if button11["text"] == button12["text"] == button13["text"] == "X":
        button11["bg"] = button12["bg"] = button13["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button21["text"] == button22["text"] == button23["text"] == "X":
        button21["bg"] = button22["bg"] = button23["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button31["text"] == button32["text"] == button33["text"] == "X":
        button31["bg"] = button32["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button11["text"] == button21["text"] == button31["text"] == "X":
        button11["bg"] = button21["bg"] = button31["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button12["text"] == button22["text"] == button32["text"] == "X":
        button12["bg"] = button22["bg"] = button32["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button13["text"] == button23["text"] == button33["text"] == "X":
        button31["bg"] = button23["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button11["text"] == button22["text"] == button33["text"] == "X":
        button11["bg"] = button22["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
    elif button13["text"] == button22["text"] == button31["text"] == "X":
        button13["bg"] = button22["bg"] = button31["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player X is the Winner")
        
    # O Conditions
    if button11["text"] == button12["text"] == button13["text"] == "O":
        button11["bg"] = button12["bg"] = button13["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button21["text"] == button22["text"] == button23["text"] == "O":
        button21["bg"] = button22["bg"] = button23["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button31["text"] == button32["text"] == button33["text"] == "O":
        button31["bg"] = button32["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button11["text"] == button21["text"] == button31["text"] == "O":
        button11["bg"] = button21["bg"] = button31["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button12["text"] == button22["text"] == button32["text"] == "O":
        button12["bg"] = button22["bg"] = button32["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button13["text"] == button23["text"] == button33["text"] == "O":
        button31["bg"] = button23["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button11["text"] == button22["text"] == button33["text"] == "O":
        button11["bg"] = button22["bg"] = button33["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")
    elif button13["text"] == button22["text"] == button31["text"] == "O":
        button13["bg"] = button22["bg"] = button31["bg"] = "#0BF616"
        messagebox.showinfo("Game End", "Player O is the Winner")


root = Tk()

root.title("X & O Game")

root.geometry("400x500")

root.geometry("+500+30")

root.configure(bg="#fafbfc")

reset_btn = Button(root, text="Reset Game", bg="#23EBAE", fg="black", font=("monospace", 20, "bold"),
                   command=lambda: reset_game())
reset_btn.place(x=110, y=30)

my_font = ("monospace", 26, "bold")

# First Row
button11 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button11))
button11.place(x=30, y=120, width=100, height=100)

button12 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button12))
button12.place(x=150, y=120, width=100, height=100)

button13 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button13))
button13.place(x=270, y=120, width=100, height=100)

# Second Row
button21 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button21))
button21.place(x=30, y=240, width=100, height=100)

button22 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button22))
button22.place(x=150, y=240, width=100, height=100)

button23 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button23))
button23.place(x=270, y=240, width=100, height=100)

# Third Row
button31 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button31))
button31.place(x=30, y=360, width=100, height=100)

button32 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button32))
button32.place(x=150, y=360, width=100, height=100)

button33 = Button(root, text="", bg="#aaaaaa", fg="black", font=my_font, command=lambda: on_btn_pressed(button33))
button33.place(x=270, y=360, width=100, height=100)

root.mainloop()

# from tkinter import *
# from tkinter import messagebox
#
# current_player = "X"
#
# player_count = 1
#
#
# def on_btn_pressed(btn):
#     global current_player, player_count
#     btn['text'] = current_player
#     player_count = player_count + 1
#     check_winner()
#     if current_player == "X":
#         current_player = "O"
#     else:
#         current_player = "X"
#
#
# def reset_game():
#     global current_player, player_count
#     current_player = "X"
#     player_count = 1
#
#     button11["text"] = button12["text"] = button13["text"] = button21["text"] = button22["text"] = button23["text"] = \
#         button31["text"] = button32["text"] = button33["text"] = ""
#
#     button11["bg"] = button12["bg"] = button13["bg"] = button21["bg"] = button22["bg"] = button23["bg"] = \
#         button31["bg"] = button32["bg"] = button33["bg"] = "#aaaaaa"
#
#
# def check_winner():
#     # X Conditions
#     if button11["text"] == button12["text"] == button13["text"] == "X":
#         button11["bg"] = button12["bg"] = button13["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button21["text"] == button22["text"] == button23["text"] == "X":
#         button21["bg"] = button22["bg"] = button23["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button31["text"] == button32["text"] == button33["text"] == "X":
#         button31["bg"] = button32["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button11["text"] == button21["text"] == button31["text"] == "X":
#         button11["bg"] = button21["bg"] = button31["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button12["text"] == button22["text"] == button32["text"] == "X":
#         button12["bg"] = button22["bg"] = button32["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button13["text"] == button23["text"] == button33["text"] == "X":
#         button13["bg"] = button23["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button11["text"] == button22["text"] == button33["text"] == "X":
#         button11["bg"] = button22["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
#     elif button13["text"] == button22["text"] == button31["text"] == "X":
#         button13["bg"] = button22["bg"] = button31["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player X is the Winner")
#
# # O Condition
#     elif button11["text"] == button12["text"] == button13["text"] == "O":
#         button11["bg"] = button12["bg"] = button13["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button21["text"] == button22["text"] == button23["text"] == "O":
#         button21["bg"] = button22["bg"] = button23["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button31["text"] == button32["text"] == button33["text"] == "O":
#         button31["bg"] = button32["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button11["text"] == button21["text"] == button31["text"] == "O":
#         button11["bg"] = button21["bg"] = button31["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button12["text"] == button22["text"] == button32["text"] == "O":
#         button12["bg"] = button22["bg"] = button32["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button13["text"] == button23["text"] == button33["text"] == "O":
#         button13["bg"] = button23["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button11["text"] == button22["text"] == button33["text"] == "O":
#         button11["bg"] = button22["bg"] = button33["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#     elif button13["text"] == button22["text"] == button31["text"] == "O":
#         button13["bg"] = button22["bg"] = button31["bg"] = "#10E310"
#         messagebox.showinfo("Game End", "Player O is the Winner")
#
#
# root = Tk()
#
# root.title("X & O Game")
#
# root.geometry("400x500")
#
# root.geometry("+450+50")
#
# root.configure(bg="#218BE8")
#
# reset_btn = Button(root, text="Reset Game", bg="#23EBAE", fg="black", font=("monospace", 20, "bold"),
#                    command=lambda: reset_game())
#
# reset_btn.place(x=110, y=30)
#
# btn_font = ("monospace", 30, "bold")
#
# # First Row Buttons
# button11 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button11))
# button11.place(x=30, y=120, width=100, height=100)
#
# button12 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button12))
# button12.place(x=150, y=120, width=100, height=100)
#
# button13 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button13))
# button13.place(x=270, y=120, width=100, height=100)
#
# # Second Row Buttons
# button21 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button21))
# button21.place(x=30, y=250, width=100, height=100)
#
# button22 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button22))
# button22.place(x=150, y=250, width=100, height=100)
#
# button23 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button23))
# button23.place(x=270, y=250, width=100, height=100)
#
# # Third Row Buttons
# button31 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button31))
# button31.place(x=30, y=380, width=100, height=100)
#
# button32 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button32))
# button32.place(x=150, y=380, width=100, height=100)
#
# button33 = Button(root, text="", bg="#aaaaaa", fg="white", font=btn_font, command=lambda: on_btn_pressed(button33))
# button33.place(x=270, y=380, width=100, height=100)
#
# root.mainloop()
#
#
#
#
#
