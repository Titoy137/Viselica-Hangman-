from tkinter import *
import tkinter as tk
import random
import time
from threading import Thread
from tkinter import filedialog
from tkinter import messagebox
import pycaw.pycaw as pycaw
from playsound import playsound

#звук неотгаданной буквы
def play():
    playsound("music/false.mp3")

#звук отгаданной буквы
def playgood():
    playsound("music/true.mp3")

#звук выйгрыша
def win_play():
    playsound("music/win.mp3")

#звук проигрыша
def lose_play():
    playsound("music/lose.mp3")

#звук назад
def back():
    playsound("music/back.mp3")

#звук следующее
def next():
    playsound("music/next.mp3")

#звук пустой
def empty():
    playsound("music/empty.wav")


def on_closing():
    mutesound()
    window.destroy()


def pravila():
    global frame_pr, backbt
    canvas.delete("all")
    framemen.destroy()
    program_namelb.destroy()
    foto.place_forget()
    pravilabt.place_forget()

    Thread(target=next, daemon=True).start()
    frame_pr = tk.Frame(window, bg='#6A5ACD', highlightbackground="black", highlightthickness=5)
    frame_pr.place(y=200, relx=0.5, rely=0.2, anchor="center")
    pravilalb = tk.Label(frame_pr, text="\nИгра 'Hangman' заключается в том, чтобы отгадать загаданное слово,\n"
                                      "угадывая по одной букве за ход.\n"
                                      " Если игрок угадывает букву, то она отображается на месте,\n"
                                      "где она находится в слове, если не угадывает, то к виселице добавляется одна\n"
                                      "часть тела человека. Игрок проигрывает, "
                                        "если виселица будет полностью нарисована,\n"
                                      "а он не отгадал слово.\nУправление производится мышкой.\n"
                                      "Красный цвет - неугаданная буква\nЗелёный цвет - угаданная букв\n"
                                      "Жёлтый цвет - буквы, которые не вычитают попытки.\n\n\n", font=("Arial", 23),
                         bg='#6A5ACD')
    pravilalb.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
    backbt = tk.Button(window, text='Вернуться', font=("Arial", 20), bg='#FAEBD7', command=backk)
    backbt.place(y=550, x=675, anchor='center')


def sound():
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Hangman.exe":
            volume.SetMute(True, None)

    soundbt.place_forget()
    soundbt1.place(relx=0.015, rely=0.02, anchor="nw")


def mutesound():
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Hangman.exe":
            volume.SetMute(False, None)

    soundbt1.place_forget()
    soundbt.place(relx=0.015, rely=0.02, anchor="nw")


# рисуем виселицу
def start_palki():
    canvas.create_line(600, 400, 900, 400, width=15, fill='#A0522D')
    canvas.create_line(750, 400, 750, 50, width=15, fill='#A0522D')
    canvas.create_line(750, 50, 850, 50, width=15, fill='#A0522D')



def difficulties(txt, tem):
    global temma, nazvanie, difbt0, difbt1, difbt2, difbt3, difbt4, frame_dif
    Thread(target=next, daemon=True).start()
    program_namelb.destroy()
    foto.place_forget()
    framemen.destroy()
    pravilabt.place_forget()

    frame_dif = tk.Frame(window, bg='#6A5ACD')
    frame_dif.grid(row=0, column=0, pady=20, padx=200, columnspan=1, rowspan=5, sticky="nsew")

    difbt0 = tk.Button(frame_dif, text='Очень легко\n(Бесконечное открытие букв)', compound=RIGHT,
                       bg='#1E90FF', font='Arial 20', command=lambda: start_chtoto(0, 34), width=950, height=3)

    difbt1 = tk.Button(frame_dif, text='Легко\n(5 бесплатных букв, 2 открытие буквы)', compound=RIGHT, bg='#008000',
                       font='Arial 20', command=lambda: start_chtoto(5, 2), width=950, height=3)

    difbt2 = tk.Button(frame_dif, text='Нормально\n(3 бесплатные буквы, 1 открытие буквы)', compound=RIGHT,
                       bg='#ffff40',
                       font='Arial 20', command=lambda: start_chtoto(3, 1), width=950, height=3)

    difbt3 = tk.Button(frame_dif, text='Сложно\n(1 открытие буквы)', compound=RIGHT, bg='#DC143C', font='Arial 20',
                       command=lambda: start_chtoto(0, 1), width=950, height=3)

    difbt4 = tk.Button(frame_dif, text='Очень сложно\n(Нет помощи)', compound=RIGHT, bg='#8B0000', font='Arial 20',
                       command=lambda: start_chtoto(0, 0), width=950, height=3)

    difbt0.grid(row=0, column=0, pady=10)
    difbt1.grid(row=1, column=0, pady=10)
    difbt2.grid(row=2, column=0, pady=10)
    difbt3.grid(row=3, column=0, pady=10)
    difbt4.grid(row=4, column=0, pady=10)

    frame_dif.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    for yy in range(5):
        window.grid_rowconfigure(yy, weight=1)
        frame_dif.grid_rowconfigure(yy, weight=1)
    temma = txt
    nazvanie = tem


def draw(lives):
    if lives == 6:
        time.sleep(0.2)
        canvas.create_line(850, 50, 850, 110, width=5, fill='black')

    elif lives == 5:
        time.sleep(0.2)
        canvas.create_oval(850, 90, 890, 140, width=8, fill='#6A5ACD', outline='black')

    elif lives == 4:
        time.sleep(0.2)
        canvas.create_oval(840, 140, 870, 230, width=10, fill='#6A5ACD', outline='black')

    elif lives == 3:
        time.sleep(0.2)
        canvas.create_line(845, 150, 830, 210, width=8, fill='black')

    elif lives == 2:
        time.sleep(0.2)
        canvas.create_line(865, 150, 875, 210, width=5, fill='black')

    elif lives == 1:
        time.sleep(0.2)
        canvas.create_line(850, 230, 840, 280, width=8, fill='black')

    elif lives == 0:
        time.sleep(0.2)
        canvas.create_line(865, 220, 870, 280, width=8, fill='black')
        game_over("lose")
        Thread(target=lose_play, daemon=True).start()


def game_over(status):
    global konecbt, program_nameelb, koneclb, koneclb2, koneclb3, nn

    if status == 'win':

        frame.destroy()
        helpbt.destroy()
        temalb.destroy()
        canvas.delete("all")
        homebt.place_forget()
        nn = 0
        koneclb = tk.Label(window, text=f'{mem}', font=("Arial", 30), bg='#6A5ACD')
        koneclb.place(relx=0.5, rely=0.2, anchor="center")

        koneclb2 = tk.Label(window, text=f'Загаданное слово:{slovo}', font=("Arial", 30), bg='#6A5ACD')
        koneclb2.place(relx=0.5, rely=0.3, anchor="center")

        program_nameelb = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
        program_nameelb.place(relx=0.5, rely=0.1, anchor="center")

        Thread(target=win_play, daemon=True).start()

        konecbt = Button(window, text='Начать заново', bg='black', foreground='white', font='Arial 16',
                         command=restart_program)
        konecbt.place(relx=0.5, rely=0.5, anchor="center")

        koneclb3 = tk.Label(window, font=('Arial', 30), text='А ты не плох,\nс победой', bg='#6A5ACD')
        koneclb3.place(relx=0.5, rely=0.4, anchor="center")

    elif status == 'lose':

        frame.destroy()
        helpbt.destroy()
        temalb.destroy()
        canvas.delete("all")
        homebt.place_forget()
        nn = 0
        program_nameelb = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
        program_nameelb.place(relx=0.5, rely=0.1, anchor="center")

        koneclb = tk.Label(window, text=f'{mem}', font=("Arial", 30), bg='#6A5ACD')
        koneclb.place(relx=0.5, rely=0.2, anchor="center")

        koneclb2 = tk.Label(window, text=f'Загаданное слово:{slovo}', font=("Arial", 30), bg='#6A5ACD')
        koneclb2.place(relx=0.5, rely=0.3, anchor="center")

        konecbt = Button(window, text='Начать заново', bg='black', foreground='white', font='Arial 16',
                         command=restart_program)
        konecbt.place(relx=0.5, rely=0.5, anchor="center")

        koneclb3 = tk.Label(window, font=('Arial', 30), text='Получится в следующий раз)', bg='#6A5ACD')
        koneclb3.place(relx=0.5, rely=0.4, anchor="center")


def restart_program():
    Thread(target=next, daemon=True).start()
    konecbt.destroy()
    program_nameelb.destroy()
    koneclb.destroy()
    koneclb2.destroy()
    koneclb3.destroy()
    canvas.delete("all")
    global lives
    lives = 7
    menu()


def backk():
    frame_pr.destroy()
    backbt.destroy()
    Thread(target=back, daemon=True).start()
    menu()


def restart_programhome():
    global nn
    Thread(target=back, daemon=True).start()
    frame.destroy()
    temalb.destroy()
    helpbt.destroy()
    canvas.delete("all")
    global lives
    lives = 7
    homebt.place_forget()
    nn = 0
    menu()


def nachalo():
    delet = [program_namelb, menubt1, menubt2, menubt3, menubt3, menubt4, menubt5, menubt6, menubt7, menubt8, menubt9,
             menubt]
    for object_name in delet:
        object_name.destroy()
    canvas.delete("all")
    foto.place_forget()
    framemen.destroy()
    frame_dif.destroy()
    difbt0.destroy()
    difbt1.destroy()
    difbt2.destroy()
    difbt3.destroy()
    difbt4.destroy()
    start_palki()


def nachalo_svoe():
    delet = [program_namelb, menubt1, menubt2, menubt3, menubt3, menubt4, menubt5, menubt6, menubt7, menubt8, menubt9,
             menubt]
    for object_name in delet:
        object_name.destroy()
    canvas.delete("all")
    foto.place_forget()
    framemen.destroy()
    start_palki()


def menu():
    global program_namelb, menubt1, menubt2, menubt3, menubt4, menubt5, menubt6, menubt7, menubt8, menubt9, menubt, framemen

    program_namelb = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
    program_namelb.place(y=450, relx=0.5, rely=0.2, anchor="center")

    framemen = tk.Frame(window, bg='#6A5ACD')
    framemen.place(y=50, relx=0.015, rely=0.02, anchor='nw')

    menubt1 = tk.Button(framemen, text='Фрукты', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("frukti.txt", "Тема:Фрукты"))
    menubt1.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

    menubt2 = tk.Button(framemen, text='Животные', bg='#FAEBD7', foreground='black', font='Arial 16', width=15,
                        height=1,
                        command=lambda: difficulties("zhivotnie.txt", "Тема:Животные"))
    menubt2.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

    menubt3 = tk.Button(framemen, text='Спорт', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("sport.txt", "Тема:Спорт"))
    menubt3.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

    menubt4 = tk.Button(framemen, text='Профессии', bg='#FAEBD7', foreground='black', font='Arial 16', width=15,
                        height=1,
                        command=lambda: difficulties("professii.txt", "Тема:Профессии"))
    menubt4.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

    menubt5 = tk.Button(framemen, text='Одежда', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("odezhda.txt", "Тема:Одежда"))
    menubt5.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')

    menubt6 = tk.Button(framemen, text='Города', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("goroda.txt", "Тема:Города"))
    menubt6.grid(row=2, column=1, padx=20, pady=20, sticky='nsew')

    menubt7 = tk.Button(framemen, text='Страны', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("strani.txt", "Тема:Страны"))
    menubt7.grid(row=3, column=0, padx=20, pady=20, sticky='nsew')

    menubt8 = tk.Button(framemen, text='Овощи', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                        command=lambda: difficulties("ovoshi.txt", "Тема:Овощи"))
    menubt8.grid(row=3, column=1, padx=20, pady=20, sticky='nsew')

    menubt9 = tk.Button(framemen, text='Случайное слово', bg='#FAEBD7', foreground='black', font='Arial 16', width=15,
                        height=1,
                        command=lambda: difficulties("rand.txt", "Тема:Случайное слово"))
    menubt9.grid(row=4, column=0, padx=20, pady=20, sticky='nsew')

    menubt = tk.Button(framemen, text='Загрузить свои', bg='#FAEBD7', foreground='black', width=15, height=1,
                       font='Arial 16', command=select_file)
    menubt.grid(row=4, column=1, padx=20, pady=20, sticky='nsew')

    soundbt.place(relx=0.015, rely=0.02, anchor='nw')
    pravilabt.place(x=50, relx=0.015, rely=0.02, anchor='nw')
    foto.place(y=160, relx=0.5, rely=0.2, anchor="center")


def helping(word, letters, n):
    global nn
    Thread(target=next, daemon=True).start()
    # Проверяем, есть ли не открытые буквы в слове
    if '_' in opened_letters:
        # Ищем буквы, которые еще не открыты и встречаются в слове
        unrevealed_letters = set([l for l in word if l not in opened_letters])
        # Если такие буквы есть, открываем первую найденную
        if unrevealed_letters:
            letter_to_reveal = unrevealed_letters.pop()
            opened_letters[opened_letters.index('_')] = letter_to_reveal
            for i, l in enumerate(word):
                if l == letter_to_reveal:
                    labels[i].config(text=letter_to_reveal)
            buttons[letters.index(letter_to_reveal)].config(bg='green')
            buttons[letters.index(letter_to_reveal)].config(state=tk.DISABLED)
            nn += 1
            if nn >= n:
                helpbt.config(state=tk.DISABLED)
            if all(label.cget('text') != '_' for label in labels):
                game_over("win")


def select_file():
    Thread(target=next, daemon=True).start()
    result = messagebox.askyesno(title='Предупреждение', message='Загрузите файл в текстовом(.txt) формате'
                                                                 '\nСлова должны быть либо в строку'
                                                                 ' через пробел, либо через Enter.'
                                                                 '\nСлова должны быть на русском алфавите,'
                                                                 '\nесли в словах будут числа или другие знаки,'
                                                                 ' то вы просто не сможете отгадать слово.)'
                                                                 '\nВсе в ваших руках!')
    if result:
        try:
            global wordsvoe
            # Открываем диалоговое окно выбора файла и получаем путь к выбранному файлу
            file_pathh = filedialog.askopenfilename()
            if file_pathh:
                # Если файл выбран, выбираем случайную строку из него и затем случайное слово из этой строки
                linesvoe = random_line(file_pathh)
                wordsvoe = random.choice(linesvoe.split()).upper()
                print(wordsvoe)
                start_svoe()
        except:
            messagebox.showerror('Ошибка', 'Этот файл либо совсем не соответсвует, либо имеет внутри'
                                           ' себя некорректное слово!')


def random_line(filename):
    with open(filename, encoding='utf-8') as f:
        lines = [line for line in f.readlines() if any(('А' <= c <= 'Я' or 'а' <= c <= 'я' or c == '-') for c in line)]
        return random.choice(lines).strip()


def start_svoe():
    nachalo_svoe()
    global mem, slovo, temalb, labels, helpbt, buttons, frame

    mem = 'Тема:Свои слова'
    temalb = tk.Label(font=('Arial', 20), text='Тема:Свои слова', foreground='white', bg='#6A5ACD')
    temalb.grid(row=0, column=0, pady=60, padx=20, sticky="nw")
    window.grid_columnconfigure(0, weight=1)

    slovo = f'{wordsvoe}'

    frame = tk.Frame(window, bg='#6A5ACD')
    frame.grid(row=3, column=0, columnspan=14, rowspan=2, pady=20, sticky="s")

    for zzz in range(2):
        frame.grid_rowconfigure(zzz, weight=1)
        window.grid_rowconfigure(zzz, weight=1)
    for zzzz in range(14):
        frame.grid_columnconfigure(zzzz, weight=1)
        window.grid_columnconfigure(zzzz, weight=1)

    homebt.place(x=100, relx=0.015, rely=0.02, anchor='nw')

    helpbt = tk.Button(window, text='Помощь', command=lambda: helping(wordsvoe, letters, 1))
    helpbt.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')

    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'
    global opened_letters
    opened_letters = ['_' for _ in range(len(wordsvoe))]

    labels = []
    for i in range(len(wordsvoe)):
        label = tk.Label(frame, text='_', font=('Arial', 20), fg='white', bg='#6A5ACD')
        label.grid(row=0, column=i, padx=5, pady=5)
        labels.append(label)

    buttons = []
    yellow_indexes = random.sample(range(len(letters)), 3)  # выбираем 3 рандомных индекса
    for i, letter in enumerate(letters):
        bg_color = '#FAEBD7'
        if i in yellow_indexes:
            bg_color = 'yellow'
        btn = tk.Button(frame, text=letter,
                        command=lambda letter=letter, btn=bin: highlight_letter(),
                        width=5, height=2, font=('Arial', 12), bg=bg_color, foreground='black')
        row = i // 17
        col = i % 17
        btn.grid(row=row + 1, column=col, padx=5, pady=5)
        buttons.append(btn)

        btn.is_highlighted = False

        def highlight_letter(btn=btn):
            global opened_letters
            # Функция, которая подсвечивает кнопку, если буква есть в слове
            letter = btn.cget('text')

            if letter in wordsvoe:
                btn.config(bg='green')
                btn.config(state=tk.DISABLED)
                Thread(target=playgood, daemon=True).start()
                # Обновляем состояние opened_letters
                for i, l in enumerate(wordsvoe):
                    if l == letter:
                        opened_letters[i] = letter
                        labels[i].config(text=letter)
                if all(label.cget('text') != '_' for label in labels):
                    game_over("win")
            elif btn.config('bg')[-1] != 'yellow':
                Thread(target=play, daemon=True).start()
                btn.config(bg='red')
                btn.config(state=tk.DISABLED)
                global lives
                lives -= 1
                draw(lives)
            else:
                btn.config(state=tk.DISABLED)
                btn.config(bg='red')

        btn.config(command=highlight_letter)


def start_chtoto(dif, n):
    nachalo()
    global mem, slovo, temalb, labels, helpbt, buttons, frame
    Thread(target=next, daemon=True).start()
    mem = f'{nazvanie}'
    temalb = tk.Label(font=('Arial', 20), text=f'{nazvanie}', foreground='white', bg='#6A5ACD')
    temalb.grid(row=0, column=0, pady=60, padx=20, sticky="nw")
    window.grid_columnconfigure(0, weight=1)

    def random_line(filename):
        with open(filename, encoding='utf-8') as f:
            return random.choice(f.readlines()).strip()

    line = random_line(f'txt\{temma}')
    word = random.choice(line.split()).upper()
    print(word)
    slovo = f'{word}'

    frame = tk.Frame(window, bg='#6A5ACD')
    frame.grid(row=3, column=0, columnspan=14, rowspan=2, pady=20, sticky="s")

    for zzz in range(2):
        frame.grid_rowconfigure(zzz, weight=1)
        window.grid_rowconfigure(zzz, weight=1)
    for zzzz in range(14):
        frame.grid_columnconfigure(zzzz, weight=1)
        window.grid_columnconfigure(zzzz, weight=1)

    homebt.place(x=50, relx=0.015, rely=0.02, anchor='nw')

    if n != 0:
        helpbt = tk.Button(window, text='Помощь', command=lambda: helping(word, letters, n))
        helpbt.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')
    else:
        helpbt = tk.Button(window, text='Помощь')
        helpbt.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')
        helpbt.config(state=tk.DISABLED)

    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'
    global opened_letters
    opened_letters = ['_' for _ in range(len(word))]
    # Создаем полоски, равное кол-ву букв в слове
    labels = []
    for i in range(len(word)):
        label = tk.Label(frame, text='_', font=('Arial', 20), fg='white', bg='#6A5ACD')
        label.grid(row=0, column=i, padx=5, pady=5)
        labels.append(label)

    buttons = []
    yellow_indexes = random.sample(range(len(letters)), dif)  # выбираем 3 рандомных индекса
    for i, letter in enumerate(letters):
        bg_color = '#FAEBD7'
        if i in yellow_indexes:
            bg_color = 'yellow'
        btn = tk.Button(frame, text=letter,
                        command=lambda letter=letter, btn=bin: highlight_letter(),
                        width=5, height=2, font=('Arial', 12), bg=bg_color, foreground='black')
        row = i // 17
        col = i % 17
        btn.grid(row=row + 1, column=col, padx=5, pady=5)
        buttons.append(btn)

        btn.is_highlighted = False

        def highlight_letter(btn=btn):
            global opened_letters
            # Функция, которая подсвечивает кнопку, если буква есть в слове
            letter = btn.cget('text')

            if letter in word:
                btn.config(bg='green')
                btn.config(state=tk.DISABLED)
                Thread(target=playgood, daemon=True).start()
                # Обновляем состояние opened_letters
                for i, l in enumerate(word):
                    if l == letter:
                        opened_letters[i] = letter
                        labels[i].config(text=letter)
                if all(label.cget('text') != '_' for label in labels):
                    game_over("win")
            elif btn.config('bg')[-1] != 'yellow':
                Thread(target=play, daemon=True).start()
                btn.config(bg='red')
                btn.config(state=tk.DISABLED)
                global lives
                lives -= 1
                draw(lives)
            else:
                btn.config(state=tk.DISABLED)
                btn.config(bg='red')

        btn.config(command=highlight_letter)


# окно игры
window = tk.Tk()
window.wm_minsize(1200, 600)

lives = 7

window.title('Hangman')

window.iconphoto(True, tk.PhotoImage(file=r"hangman.png"))

window["bg"] = '#6A5ACD'

window.geometry('1350x700')

canvas = Canvas(window, bg='#6A5ACD', height=1080, width=1920, highlightthickness=0)
canvas.place(x=0, y=0)

photo1 = PhotoImage(file=r"mute.png")
photo = PhotoImage(file=r"audio-speaker-on.png")
photo2 = PhotoImage(file=r'home-icon-silhouette.png')
photo3 = PhotoImage(file=r'question.png')

nn = 0

soundbt = tk.Button(image=photo, bg='#FAEBD7', command=sound)

soundbt1 = tk.Button(image=photo1, bg='#FAEBD7', command=mutesound)

pravilabt = tk.Button(image=photo3, bg='#FAEBD7', command=pravila)

homebt = tk.Button(text='Сменить тему', image=photo2, compound=LEFT, command=restart_programhome)

image = tk.PhotoImage(file=r"man.png").subsample(3)

foto = Label(window, image=image, bg='#6A5ACD')

window.protocol("WM_DELETE_WINDOW", on_closing)

menu()
Thread(target=empty, daemon=True).start()
window.mainloop()
