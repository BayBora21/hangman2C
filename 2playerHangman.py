import tkinter as tk

import random
# from PIL import Image, ImageTk
# import requests
import os
import sys

Country_Data = "Turkey"
Animal_Data = "Bird"
Capital_Data = "Ankara"
Fruit_Data = "Mango"

window = tk.Tk()
window.geometry("1600x900")
window.title("Hangman Game")
window.configure(bg="#1B1B1B")
window.resizable(False, False)

window_x = int((window.winfo_screenwidth() / 2) - (1600 / 2))
window_y = int((window.winfo_screenheight() / 2) - (900 / 2))
window_geometry = str(1600) + 'x' + str(900) + '+' + str(window_x) + '+' + str(window_y)
window.geometry(window_geometry)

icon = tk.PhotoImage(file="Photo/icon/icon.ico")
window.iconphoto(True, icon)


global canvas
canvas = tk.Canvas(window, width=1600, height=900, bg="#1B1B1B")
canvas.pack()
canvas.create_line(640, 100, 960, 100, fill="green", width=5)
canvas.create_line(645, 105, 955, 105, fill="black", width=3)
canvas.create_line(642, 100, 642, 530, fill="green", width=5)
canvas.create_line(647, 105, 647, 527, fill="black", width=3)
canvas.create_line(957, 100, 957, 530, fill="green", width=5)
canvas.create_line(962, 97, 962, 535, fill="black", width=3)
canvas.create_line(640, 530, 960, 530, fill="green", width=5)
canvas.create_line(645, 535, 964, 535, fill="black", width=3)
tk.Label(window, text="player 1 turn", font=("Ariel", 30), bg="#1B1B1B", fg="green").place(x=670, y=34)

global turn_counter
turn_counter = 0


def keyboard():
            keyboard_button_a = tk.Button(window,
                                          text="a",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command= lambda: random_country_class.clicked_key(0))
            keyboard_button_a.place(relx=0.44, rely=0.2, anchor=tk.CENTER)

            keyboard_button_b = tk.Button(window,
                                text="b",
                                background="black",
                                foreground="green",
                                font=("Ariel", 16),
                                activebackground="black",
                                activeforeground="white",
                                borderwidth="3",
                                padx="4px",
                                command= lambda: random_country_class.clicked_key(1))
            keyboard_button_b.place(relx=0.47, rely=0.2, anchor=tk.CENTER)

            keyboard_button_c = tk.Button(window,
                                          text="c",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(2))
            keyboard_button_c.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

            keyboard_button_d = tk.Button(window,
                                          text="d",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(3))
            keyboard_button_d.place(relx=0.53, rely=0.2, anchor=tk.CENTER)

            keyboard_button_e = tk.Button(window,
                                          text="e",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(4))
            keyboard_button_e.place(relx=0.56, rely=0.2, anchor=tk.CENTER)

            keyboard_button_f = tk.Button(window,
                                          text="f ",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="3px",
                                          command=lambda: random_country_class.clicked_key(5))
            keyboard_button_f.place(relx=0.44, rely=0.26, anchor=tk.CENTER)

            keyboard_button_g = tk.Button(window,
                                          text="g",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="3px",
                                          command=lambda: random_country_class.clicked_key(6))
            keyboard_button_g.place(relx=0.47, rely=0.26, anchor=tk.CENTER)


            keyboard_button_h = tk.Button(window,
                                          text="h",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="3px",
                                          command=lambda: random_country_class.clicked_key(7))
            keyboard_button_h.place(relx=0.50, rely=0.26, anchor=tk.CENTER)

            keyboard_button_i = tk.Button(window,
                                          text="i",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="6px",
                                          command=lambda: random_country_class.clicked_key(8))
            keyboard_button_i.place(relx=0.53, rely=0.26, anchor=tk.CENTER)

            keyboard_button_j = tk.Button(window,
                                          text="j",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="5px",
                                          command=lambda: random_country_class.clicked_key(9))
            keyboard_button_j.place(relx=0.56, rely=0.26, anchor=tk.CENTER)

            keyboard_button_k = tk.Button(window,
                                          text="k",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(10))
            keyboard_button_k.place(relx=0.44, rely=0.32, anchor=tk.CENTER)

            keyboard_button_l = tk.Button(window,
                                          text="l",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="6px",
                                          command=lambda: random_country_class.clicked_key(11))
            keyboard_button_l.place(relx=0.47, rely=0.32, anchor=tk.CENTER)

            keyboard_button_m = tk.Button(window,
                                          text="m",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="1px",
                                          command=lambda: random_country_class.clicked_key(12))
            keyboard_button_m.place(relx=0.50, rely=0.32, anchor=tk.CENTER)

            keyboard_button_n = tk.Button(window,
                                          text="n",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="3px",
                                          command=lambda: random_country_class.clicked_key(13))
            keyboard_button_n.place(relx=0.53, rely=0.32, anchor=tk.CENTER)

            keyboard_button_o = tk.Button(window,
                                          text="o",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(14))
            keyboard_button_o.place(relx=0.56, rely=0.32, anchor=tk.CENTER)

            keyboard_button_p = tk.Button(window,
                                          text="p",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="3px",
                                          command=lambda: random_country_class.clicked_key(15))
            keyboard_button_p.place(relx=0.44, rely=0.38, anchor=tk.CENTER)

            keyboard_button_q = tk.Button(window,
                                          text="q",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(16))
            keyboard_button_q.place(relx=0.47, rely=0.38, anchor=tk.CENTER)

            keyboard_button_r = tk.Button(window,
                                          text="r",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(17))
            keyboard_button_r.place(relx=0.50, rely=0.38, anchor=tk.CENTER)

            keyboard_button_s = tk.Button(window,
                                          text="s",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(18))
            keyboard_button_s.place(relx=0.53, rely=0.38, anchor=tk.CENTER)

            keyboard_button_t = tk.Button(window,
                                          text="t",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(19))
            keyboard_button_t.place(relx=0.56, rely=0.38, anchor=tk.CENTER)

            keyboard_button_u = tk.Button(window,
                                          text="u",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(20))
            keyboard_button_u.place(relx=0.44, rely=0.44, anchor=tk.CENTER)

            keyboard_button_v = tk.Button(window,
                                          text="v",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(21))
            keyboard_button_v.place(relx=0.47, rely=0.44, anchor=tk.CENTER)

            keyboard_button_w = tk.Button(window,
                                          text="w",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(22))
            keyboard_button_w.place(relx=0.50, rely=0.44, anchor=tk.CENTER)

            keyboard_button_x = tk.Button(window,
                                          text="x",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(23))
            keyboard_button_x.place(relx=0.53, rely=0.44, anchor=tk.CENTER)

            keyboard_button_y = tk.Button(window,
                                          text="y",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(24))
            keyboard_button_y.place(relx=0.56, rely=0.44, anchor=tk.CENTER)

            keyboard_button_z = tk.Button(window,
                                          text="z",
                                          background="black",
                                          foreground="green",
                                          font=("Ariel", 16),
                                          activebackground="black",
                                          activeforeground="white",
                                          borderwidth="3",
                                          padx="4px",
                                          command=lambda: random_country_class.clicked_key(25))
            keyboard_button_z.place(relx=0.50, rely=0.50, anchor=tk.CENTER)


def category_buttons():

        country_category_button = tk.Button(window,
                                            text="Country",
                                            background="black",
                                            foreground="green",
                                            font=("Ariel", 16),
                                            activebackground="black",
                                            activeforeground="white",
                                            borderwidth="3",
                                            command=player_number_control
                                            )
        country_category_button.place(relx=0.04, rely=0.64)

        animal_category_button = tk.Button(window,
                                            text="Animals",
                                            background="black",
                                            foreground="green",
                                            font=("Ariel", 16),
                                            activebackground="black",
                                            activeforeground="white",
                                            borderwidth="3",
                                            command=player_number_control_2
                                            )
        animal_category_button.place(relx=0.12, rely=0.64)

        capital_category_button = tk.Button(window,
                                            text="Capital",
                                            background="black",
                                            foreground="green",
                                            font=("Ariel", 16),
                                            activebackground="black",
                                            activeforeground="white",
                                            borderwidth="3",
                                            command=player_number_control_3
                                            )
        capital_category_button.place(relx=0.2, rely=0.64)

        fruit_category_button = tk.Button(window,
                                            text="Fruits",
                                            background="black",
                                            foreground="green",
                                            font=("Ariel", 16),
                                            activebackground="black",
                                            activeforeground="white",
                                            borderwidth="3",
                                            command=player_number_control_4
                                            )
        fruit_category_button.place(relx=0.28, rely=0.64)

        country_category_button_2 = tk.Button(window,
                                            text="Country",
                                            background="black",
                                            foreground="green",
                                            font=("Ariel", 16),
                                            activebackground="black",
                                            activeforeground="white",
                                            borderwidth="3",
                                            command=player_number_control
                                            )
        country_category_button_2.place(relx=0.64, rely=0.64)

        animal_category_button_2 = tk.Button(window,
                                      text="Animals",
                                      background="black",
                                      foreground="green",
                                      font=("Ariel", 16),
                                      activebackground="black",
                                      activeforeground="white",
                                      borderwidth="3",
                                      command=player_number_control_2
                                      )
        animal_category_button_2.place(relx=0.72, rely=0.64)

        capital_category_button_2 = tk.Button(window,
                                      text="Capital",
                                      background="black",
                                      foreground="green",
                                      font=("Ariel", 16),
                                      activebackground="black",
                                      activeforeground="white",
                                      borderwidth="3",
                                      command=player_number_control_3
                                      )
        capital_category_button_2.place(relx=0.80, rely=0.64)

        fruit_category_button_2 = tk.Button(window,
                                      text="Fruits",
                                      background="black",
                                      foreground="green",
                                      font=("Ariel", 16),
                                      activebackground="black",
                                      activeforeground="white",
                                      borderwidth="3",
                                      command=player_number_control_4
                                      )
        fruit_category_button_2.place(relx=0.88, rely=0.64)


global png_counter, png_counter2
png_counter = 0
png_counter2 = 0
global wrong_letter_counter, wrong_letter_counter2
wrong_letter_counter = 0
wrong_letter_counter2 = 0
global winner_score, winner_score2
winner_score = 0
winner_score2 = 0

global control_number
control_number = 0
global player_number
player_number = 0
global player1_score, player2_score
player1_score = 0
player2_score = 0


def player_number_control():
    global player_number
    player_number += 1
    random_country_class.press_country_button()


def player_number_control_2():
    global player_number
    player_number += 1
    random_country_class.press_animal_button()


def player_number_control_3():
    global player_number
    player_number += 1
    random_country_class.press_capital_button()


def player_number_control_4():
    global player_number
    player_number += 1
    random_country_class.press_fruit_button()


class random_country_class():
    global winner_score
    global winner_score2

    def press_country_button():
        global selected_category, selected_category2, control_number
        if player_number == 1:
            selected_country = Country_Data.Country[random.randint(0, 201)]
            selected_category = [selected_country]
            control_number = 1
            random_country_class.random_country()
            player_turn_label()
        elif player_number == 2:
            selected_country2 = Country_Data.Country[random.randint(0, 201)]
            selected_category2 = [selected_country2]
            control_number = 1
            random_country_class.random_country()
            player_turn_label()

    def press_animal_button():
        global selected_category, selected_category2, control_number
        if player_number == 1:
            selected_animal = Animal_Data.name[random.randint(0, 526)]
            selected_category = [selected_animal]
            control_number = 2
            random_country_class.random_country()
            player_turn_label()
        elif player_number == 2:
            selected_animal2 = Animal_Data.name[random.randint(0, 526)]
            selected_category2 = [selected_animal2]
            control_number = 2
            random_country_class.random_country()
            player_turn_label()


    def press_capital_button():
        global selected_category, selected_category2, control_number
        if player_number == 1:
            selected_capital = Capital_Data.name[random.randint(0, 218)]
            selected_category = [selected_capital]
            control_number = 3
            random_country_class.random_country()
            player_turn_label()
        elif player_number == 2:
            selected_capital2 = Capital_Data.name[random.randint(0, 218)]
            selected_category2 = [selected_capital2]
            control_number = 3
            random_country_class.random_country()
            player_turn_label()


    def press_fruit_button():
        global selected_category, selected_category2, control_number
        if player_number == 1:
            selected_fruit = Fruit_Data.name[random.randint(0, 578)]
            selected_category = [selected_fruit]
            control_number = 4
            random_country_class.random_country()
            player_turn_label()
        elif player_number == 2:
            selected_fruit2 = Fruit_Data.name[random.randint(0, 578)]
            selected_category2 = [selected_fruit2]
            control_number = 4
            random_country_class.random_country()
            player_turn_label()


    def category_frame_1():
        global imga
        canvas.create_line(286, 40, 406, 40, fill="green", width=5)
        canvas.create_line(291, 45, 401, 45, fill="black", width=3)
        canvas.create_line(288, 90, 288, 40, fill="green", width=5)
        canvas.create_line(293, 88, 293, 45, fill="black", width=3)
        canvas.create_line(403, 40, 403, 90, fill="green", width=5)
        canvas.create_line(408, 40, 408, 95, fill="black", width=3)
        canvas.create_line(286, 90, 406, 90, fill="green", width=5)
        canvas.create_line(291, 95, 410, 95, fill="black", width=3)
        imga = tk.PhotoImage(file="Photo/hangman0.png")
        tk.Label(window, image=imga, width=300, height=300, bg="#1B1B1B").place(x=200, y=120)


    def category_frame_2():
        global imgb
        canvas.create_line(1186, 40, 1306, 40, fill="green", width=5)
        canvas.create_line(1191, 45, 1301, 45, fill="black", width=3)
        canvas.create_line(1188, 90, 1188, 40, fill="green", width=5)
        canvas.create_line(1193, 88, 1193, 45, fill="black", width=3)
        canvas.create_line(1303, 40, 1303, 90, fill="green", width=5)
        canvas.create_line(1308, 40, 1308, 95, fill="black", width=3)
        canvas.create_line(1186, 90, 1306, 90, fill="green", width=5)
        canvas.create_line(1191, 95, 1310, 95, fill="black", width=3)
        imgb = tk.PhotoImage(file="Photo/hangman0.png")
        tk.Label(window, image=imgb, width=300, height=300, bg="#1B1B1B").place(x=1100, y=120)


    def category_info_label():
        if turn_counter == 0:
            if control_number == 1:
                tk.Label(window, text="Country", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=300, y=50)
            if control_number == 2:
                tk.Label(window, text="Animal", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=300, y=50)
            if control_number == 3:
                tk.Label(window, text="Capital", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=300, y=50)
            if control_number == 4:
                tk.Label(window, text="Fruits", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=310, y=50)
        else:
            if control_number == 1:
                tk.Label(window, text="Country", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=1200, y=50)
            if control_number == 2:
                tk.Label(window, text="Animal", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=1200, y=50)
            if control_number == 3:
                tk.Label(window, text="Capital", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=1200, y=50)
            if control_number == 4:
                tk.Label(window, text="Fruits", font=("Ariel", 16), bg="#1B1B1B", fg="green", borderwidth="3").place(x=1200, y=50)


    def random_country():
        global turn_counter
        if turn_counter == 0 and player_number == 1:
            print(selected_category[0])
            country_letter = selected_category[0]
            list_len = int(len(selected_category[0]) - 1)
            tk.Label(window, bg="#1B1B1B", fg="green", text="Good Luck Player One", font=("Ariel", 37)).place(relx=0.04, rely=0.64)
            random_country_class.category_info_label()
            random_country_class.category_frame_1()

            turn_counter += 1

            i = 0
            while (i <= list_len):
                if (country_letter[i] == " "):
                    label1 = tk.Label(window, text="-", font=("Ariel", 16), bg="#1B1B1B", fg="white")
                    label1.place(x=100 + (i * 30), y=460)
                    i += 1
                    continue
                label2 = tk.Label(window, text=" ", bg="green", font=("Ariel", 20))
                label2.place(x=100 + (i * 30), y=460)
                label3 = tk.Label(window, text="Wrong Letters = ", fg="green", bg="#1B1B1B", font=("Ariel", 20))
                label3.place(x=100, y=530)
                i += 1
        elif turn_counter == 1 and player_number == 2:
            print(selected_category2[0])
            country_letter = selected_category2[0]
            list_len = int(len(selected_category2[0]) - 1)
            tk.Label(window, bg="#1B1B1B", fg="green", text="Good Luck Player Two", font=("Ariel", 37)).place(relx=0.62, rely=0.64)
            random_country_class.category_info_label()
            random_country_class.category_frame_2()

            turn_counter -= 1

            i = 0
            while (i <= list_len):
                if (country_letter[i] == " "):
                    label1 = tk.Label(window, text="-", font=("Ariel", 16), bg="#1B1B1B", fg="white")
                    label1.place(x=995 + (i * 30), y=460)
                    i += 1
                    continue
                label2 = tk.Label(window, text=" ", bg="green", font=("Ariel", 20))
                label2.place(x=995 + (i * 30), y=460)
                label3 = tk.Label(window, text="Wrong Letters = ", fg="green", bg="#1B1B1B", font=("Ariel", 20))
                label3.place(x=995, y=530)
                i += 1


    def clicked_key(key):
        global turn_counter
        global winner_score
        global winner_score2
        keyboard_key_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if turn_counter == 0:
            country_list = [selected_category[0]]
            country_letter = country_list[0]
            list_len = int(len(country_list[0]) - 1)
            i = 0
            a = -1
            turn_counter += 1
            player_turn_label()
            while(i <= list_len):
                if (country_letter[i] == keyboard_key_list[key] or country_letter[i] == keyboard_key_list[key].upper()):
                    label1 = tk.Label(window, text=country_letter[i], font=("Ariel", 22), bg="#1B1B1B", fg="white")
                    label1.place(x=100 + (i * 30), y=460)
                    winner_score += 1
                    winner_controler()
                    i += 1
                else:
                    a += 1

                if(a == (list_len)):
                    turn_counter -= 1
                    global wrong_letter_counter
                    number = keyboard_key_list[key]
                    wrong_letter_counter += 1
                    wrong_letters(number)

                    global png_counter
                    png_counter += 1
                    hangman_photos()
                i += 1
        else:
            country_list = [selected_category2[0]]
            country_letter = country_list[0]
            list_len = int(len(country_list[0]) - 1)
            i = 0
            a = -1
            turn_counter -= 1
            player_turn_label()
            while (i <= list_len):
                if (country_letter[i] == keyboard_key_list[key] or country_letter[i] == keyboard_key_list[key].upper()):
                    label1 = tk.Label(window, text=country_letter[i], font=("Ariel", 22), bg="#1B1B1B", fg="white")
                    label1.place(x=995 + (i * 30), y=460)
                    winner_score2 += 1
                    winner_controler()
                    i += 1
                else:
                    a += 1

                if (a == (list_len)):
                    turn_counter += 1
                    global wrong_letter_counter2
                    number = keyboard_key_list[key]
                    wrong_letter_counter2 += 1
                    wrong_letters(number)

                    global png_counter2
                    png_counter2 += 1
                    hangman_photos()
                i += 1


def player_turn_label():
    if turn_counter == 0:
        tk.Label(window, text="player 1 turn", font=("Ariel", 30), bg="#1B1B1B", fg="green").place(x=670, y=34)
    if turn_counter == 1:
        tk.Label(window, text="player 2 turn", font=("Ariel", 30), bg="#1B1B1B", fg="green").place(x=670, y=34)

def hangman_photos():
    global png_counter, turn_counter
    global png_counter2
    global img1
    global img2
    if turn_counter == 1:
        if(png_counter == 1):
            img1 = tk.PhotoImage(file="Photo/hangman1.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
        elif(png_counter == 2):
            img1 = tk.PhotoImage(file="Photo/hangman2.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
        elif(png_counter == 3):
            img1 = tk.PhotoImage(file="Photo/hangman3.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
        elif(png_counter == 4):
            img1 = tk.PhotoImage(file="Photo/hangman4.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
        elif(png_counter == 5):
            img1 = tk.PhotoImage(file="Photo/hangman5.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
        elif(png_counter == 6):
            img1 = tk.PhotoImage(file="Photo/hangman6.png")
            tk.Label(window, image=img1, width= 300, height=300, bg="#1B1B1B").place(x=200, y=120)
    else:
        if(png_counter2 == 1):
            img2 = tk.PhotoImage(file="Photo/hangman1.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)
        elif(png_counter2 == 2):
            img2 = tk.PhotoImage(file="Photo/hangman2.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)
        elif(png_counter2 == 3):
            img2 = tk.PhotoImage(file="Photo/hangman3.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)
        elif(png_counter2 == 4):
            img2 = tk.PhotoImage(file="Photo/hangman4.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)
        elif(png_counter2 == 5):
            img2 = tk.PhotoImage(file="Photo/hangman5.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)
        elif(png_counter2 == 6):
            img2 = tk.PhotoImage(file="Photo/hangman6.png")
            tk.Label(window, image=img2, width= 300, height=300, bg="#1B1B1B").place(x=1100, y=120)


def winner_controler():
    if winner_score == int(len(selected_category[0])):
        tk.Label(window, text="WINNER", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=60, y=530)
        tk.Label(window, text="   " + selected_category[0] + "         ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=70, y=460)
        tk.Label(window, text="LOSER  ", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=995, y=530)
        tk.Label(window, text=selected_category2[0] + "                 ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=995, y=460)
        global player1_score
        player1_score += 10
        restart_button_def()
    if winner_score2 == int(len(selected_category2[0])):
        tk.Label(window, text=" LOSER  ", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=60, y=530)
        tk.Label(window, text="   " + selected_category[0] + "         ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=70, y=460)
        tk.Label(window, text="WINNER", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=995, y=530)
        tk.Label(window, text=selected_category2[0] + "                 ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=995, y=460)
        global player2_score
        player2_score += 10
        restart_button_def()


def wrong_letters(n):
    global wrong_letter_counter
    global wrong_letter_counter2
    global selected_category
    global selected_category2
    global turn_counter


    if turn_counter == 0:
        turn_counter += 1
        if wrong_letter_counter == 1:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=340, y=530)
        elif wrong_letter_counter == 2:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=370, y=530)
        elif wrong_letter_counter == 3:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=400, y=530)
        elif wrong_letter_counter == 4:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=430, y=530)
        elif wrong_letter_counter == 5:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=460, y=530)
        elif wrong_letter_counter == 6:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=490, y=530)
            tk.Label(window, text=" LOSER ", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=60, y=530)
            tk.Label(window, text="   " + selected_category[0] + "       ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=70, y=460)
            tk.Label(window, text="WINNER", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=995, y=530)
            tk.Label(window, text=selected_category2[0] + "             ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=995, y=460)
            global player2_score
            player2_score += 10
            restart_button_def()


    else:
        turn_counter -= 1
        if wrong_letter_counter2 == 1:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1240, y=530)
        elif wrong_letter_counter2 == 2:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1270, y=530)
        elif wrong_letter_counter2 == 3:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1300, y=530)
        elif wrong_letter_counter2 == 4:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1330, y=530)
        elif wrong_letter_counter2 == 5:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1360, y=530)
        elif wrong_letter_counter2 == 6:
            label2 = tk.Label(window, text=n, bg="#1B1B1B", fg="white", font=("Ariel", 16))
            label2.place(x=1390, y=530)
            tk.Label(window, text="WINNER", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=60, y=530)
            tk.Label(window, text="   " + selected_category[0] + "         ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=70, y=460)
            tk.Label(window, text="LOSER  ", font=("Ariel", 90), bg="#1B1B1B", fg="white").place(x=995, y=530)
            tk.Label(window, text=selected_category2[0] + "                 ", font=("Ariel", 30), fg="white", bg="#1B1B1B").place(x=995, y=460)
            global player1_score
            player1_score += 10
            restart_button_def()

def message_box():
    toplevel = tk.Toplevel(window)

    toplevel.title("QUIT")
    x_position = 300
    y_position = 200
    toplevel.geometry(f"300x100+{x_position}+{y_position}")

    l1 = tk.Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(toplevel, text="Çıkmak istediğine emin misin?")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = tk.Button(toplevel, text="Yes", command=window.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2 = tk.Button(toplevel, text="No", command=toplevel.destroy, width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")


tk.Button(window, text="Quit", command=message_box, width=7, bg="black", fg="green").place(x=1500, y=30)


def restart_button_def():
    restart_button = tk.Button(text="Restart",
                               background="black",
                               foreground="green",
                               font=("Ariel", 40),
                               activebackground="black",
                               activeforeground="white",
                               borderwidth="3",
                               padx="4px",
                               command=restart)
    restart_button.place(relx=0.50, rely=0.72, anchor=tk.CENTER)

def restart():
    window.destroy()
    os.system('py Hangman.py')


keyboard()
category_buttons()
window.mainloop()
