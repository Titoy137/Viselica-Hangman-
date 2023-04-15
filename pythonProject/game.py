from tkinter import *
import tkinter as tk
import random
import time
from threading import Thread
from tkinter import filedialog
from tkinter import messagebox
from music import lose_play, win_play, playgood, play, back, next
import pycaw.pycaw as pycaw

def on_closing():
    msound()
    window.destroy()

def pravila(event):
    global z
    z = tk.Label(window, text="Игра 'Hangman' заключается в том, чтобы отгадать загаданное слово,\n"
                              "угадывая по одной букве за ход.\n"
                              " Если игрок угадывает букву, то она отображается на месте,\n"
                              "где она находится в слове, если не угадывает, то к виселице добавляется одна\n"
                              "часть тела человека. Игрок проигрывает, если виселица будет полностью нарисована,\n"
                              " а он не отгадал слово.\n"
                              "Управление производится мышкой.\n"
                              "Красный цвет - неугаданная буква\n"
                              "Зелёный цвет - угаданная букв\n"
                              "Жёлтый цвет - буквы, которые не вычитают попытки.", font=("Arial", 20), bg='#FAEBD7')
    z.place(y=50, relx=0.5, rely=0.2, anchor="center")

def leave_message(event):
    z.place_forget()
    zz = tk.Label(window, text="", font=("Arial", 50), bg='#6A5ACD')
    zz.place(y=50, relx=0.5, rely=0.2, anchor="center")
    zz.place_forget()

def sound():
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "python.exe":
            volume.SetMute(True, None)

    ph.place_forget()
    ph1.place(relx=0.015, rely=0.02, anchor="nw")

def msound():

    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "python.exe":
            volume.SetMute(False, None)

    ph1.place_forget()
    ph.place(relx=0.015, rely=0.02, anchor="nw")

#рисуем виселицу
def start_palki():

    canvas.create_line(600, 400, 900, 400, width=15, fill='#A0522D')
    canvas.create_line(750, 400, 750, 50, width=15, fill='#A0522D')
    canvas.create_line(750, 50, 850, 50, width=15, fill='#A0522D')

def difficulties(txt, tem):

    global temma, nazvanie
    Thread(target=next, daemon=True).start()
    program_name.destroy()
    foto.place_forget()
    framemen.destroy()

    dif0.grid(row=0, column=0, pady=10)
    dif1.grid(row=1, column=0, pady=10)
    dif2.grid(row=2, column=0, pady=10)
    dif3.grid(row=3, column=0, pady=10)
    dif4.grid(row=4, column=0, pady=10)

    window.grid_columnconfigure(0, weight=1)
    for yy in range(5):
        window.grid_rowconfigure(yy, weight=1)
    temma = txt
    nazvanie = tem


def draw(lifes):

    if lifes == 6:
        time.sleep(0.2)
        canvas.create_line(850, 50, 850, 110, width=5, fill='black')

    elif lifes == 5:
        time.sleep(0.2)
        canvas.create_oval(850, 90, 890, 140, width=8, fill='#6A5ACD', outline='black')

    elif lifes == 4:
        time.sleep(0.2)
        canvas.create_oval(840, 140, 870, 230, width=10, fill='#6A5ACD', outline='black')

    elif lifes == 3:
        time.sleep(0.2)
        canvas.create_line(845, 150, 830, 210, width=8, fill='black')

    elif lifes == 2:
        time.sleep(0.2)
        canvas.create_line(865, 150, 875, 210, width=5, fill='black')

    elif lifes == 1:
        time.sleep(0.2)
        canvas.create_line(850, 230, 840, 280, width=8, fill='black')

    elif lifes == 0:
        time.sleep(0.2)
        canvas.create_line(865, 220, 870, 280, width=8, fill='black')
        game_over("lose")
        Thread(target=lose_play, daemon=True).start()

def game_over(status):

    global bttt2, program_namee, konec, konec2, konec3, nn

    if status == 'win':

        frame.destroy()
        helpp.destroy()
        tema.destroy()
        canvas.delete("all")
        home.place_forget()
        nn = 0
        konec = tk.Label(window, text=f'{mem}', font=("Arial", 30), bg='#6A5ACD')
        konec.place(relx=0.5, rely=0.2, anchor="center")

        konec2 = tk.Label(window, text=f'Загаданное слово:{slovo}', font=("Arial", 30), bg='#6A5ACD')
        konec2.place(relx=0.5, rely=0.3, anchor="center")

        program_namee = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
        program_namee.place(relx=0.5, rely=0.1, anchor="center")

        Thread(target=win_play, daemon=True).start()

        bttt2 = Button(window, text='Начать заново',  bg='black', foreground='white', font='Arial 16',
                       command=restart_program)
        bttt2.place(relx=0.5, rely=0.5, anchor="center")

        konec3 = tk.Label(window, font=('Arial', 30), text='А ты не плох,\nс победой', bg='#6A5ACD')
        konec3.place(relx=0.5, rely=0.4, anchor="center")

    elif status == 'lose':

        frame.destroy()
        helpp.destroy()
        tema.destroy()
        canvas.delete("all")
        home.place_forget()
        nn = 0
        program_namee = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
        program_namee.place(relx=0.5, rely=0.1, anchor="center")

        konec = tk.Label(window, text=f'{mem}', font=("Arial", 30), bg='#6A5ACD')
        konec.place(relx=0.5, rely=0.2, anchor="center")

        konec2 = tk.Label(window, text=f'Загаданное слово:{slovo}', font=("Arial", 30), bg='#6A5ACD')
        konec2.place(relx=0.5, rely=0.3, anchor="center")

        bttt2 = Button(window, text='Начать заново',  bg='black', foreground='white', font='Arial 16',
                       command=restart_program)
        bttt2.place(relx=0.5, rely=0.5, anchor="center")

        konec3 = tk.Label(window, font=('Arial', 30), text='Получится в следующий раз)', bg='#6A5ACD')
        konec3.place(relx=0.5, rely=0.4, anchor="center")

def restart_program():
    Thread(target=next, daemon=True).start()
    bttt2.destroy()
    program_namee.destroy()
    konec.destroy()
    konec2.destroy()
    konec3.destroy()
    canvas.delete("all")
    global lifes
    lifes = 7
    menu()

def restart_programhome():
    global nn
    Thread(target=back, daemon=True).start()
    frame.destroy()
    tema.destroy()
    helpp.destroy()
    canvas.delete("all")
    global lifes
    lifes = 7
    home.place_forget()
    nn = 0
    menu()

def nachalo():

    delet = [program_name, bt1, bt2, bt3, bt3, bt4, bt5, bt6, bt7, bt8, bt9, btsvoe]
    for object_name in delet:
        object_name.destroy()
    canvas.delete("all")
    foto.place_forget()
    framemen.destroy()
    dif0.grid_forget()
    dif1.grid_forget()
    dif2.grid_forget()
    dif3.grid_forget()
    dif4.grid_forget()
    start_palki()

def menu():

    global program_name, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, btsvoe, framemen

    program_name = tk.Label(window, text="H A N G M A N", font=("Arial", 50), bg='#6A5ACD')
    program_name.place(y=450, relx=0.5, rely=0.2, anchor="center")

    framemen = tk.Frame(window, bg='#6A5ACD')
    framemen.place(y=50, relx=0.015, rely=0.02, anchor='nw')

    bt1 = tk.Button(framemen, text='Фрукты', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("frukti.txt", "Тема:Фрукты"))
    bt1.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

    bt2 = tk.Button(framemen, text='Животные', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("zhivotnie.txt", "Тема:Животные"))
    bt2.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

    bt3 = tk.Button(framemen, text='Спорт', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("sport.txt", "Тема:Спорт"))
    bt3.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

    bt4 = tk.Button(framemen, text='Профессии', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("professii.txt", "Тема:Профессии"))
    bt4.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

    bt5 = tk.Button(framemen, text='Одежда', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("odezhda.txt", "Тема:Одежда"))
    bt5.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')

    bt6 = tk.Button(framemen, text='Города', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("goroda.txt", "Тема:Города"))
    bt6.grid(row=2, column=1, padx=20, pady=20, sticky='nsew')

    bt7 = tk.Button(framemen, text='Страны', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("strani.txt", "Тема:Страны"))
    bt7.grid(row=3, column=0, padx=20, pady=20, sticky='nsew')

    bt8 = tk.Button(framemen, text='Овощи', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("ovoshi.txt", "Тема:Овощи"))
    bt8.grid(row=3, column=1, padx=20, pady=20, sticky='nsew')

    bt9 = tk.Button(framemen, text='Случайное слово', bg='#FAEBD7', foreground='black', font='Arial 16', width=15, height=1,
                    command=lambda: difficulties("rand.txt", "Тема:Случайное слово"))
    bt9.grid(row=4, column=0, padx=20, pady=20, sticky='nsew')

    btsvoe = tk.Button(framemen, text='Загрузить свои', bg='#FAEBD7', foreground='black', width=15, height=1,
                       font='Arial 16', command=select_file)
    btsvoe.grid(row=4, column=1, padx=20, pady=20, sticky='nsew')

    ph.place(relx=0.015, rely=0.02, anchor='nw')
    ph2.place(x=50, relx=0.015, rely=0.02, anchor='nw')
    foto.place(y=160, relx=0.5, rely=0.2, anchor="center")

def helping(word, letters, n):
    # Проверяем, есть ли не открытые буквы в слове
    global nn
    Thread(target=next, daemon=True).start()
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
                helpp.config(state=tk.DISABLED)
            if all(label.cget('text') != '_' for label in labels):
                game_over("win")

def select_file():
    Thread(target=next, daemon=True).start()
    result = messagebox.askyesno(title='Предупреждение', message='Загрузите файл в текстовом(.txt) формате'
                                                           '\nСлова должны быть либо в строку через пробел, либо через Enter.'
                                                                 '\nСлова должны быть на русском алфавите,'
                                                                 '\nесли в словах будут числа или другие знаки, то вы просто не сможете отгадать слово.)'
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
            messagebox.showerror('Ошибка', 'Это плохой файл')

def random_line(filename):

    with open(filename, encoding='utf-8') as f:
        return random.choice(f.readlines()).strip()

def start_svoe():

    nachalo()
    global mem, slovo, tema, labels, helpp, buttons

    mem = 'Тема:Свои слова'
    tema = tk.Label(font=('Arial', 20), text='Тема:Свои слова', foreground='white', bg='#6A5ACD')
    tema.grid(row=0, column=0, pady=60, padx=20, sticky="nw")
    window.grid_columnconfigure(0, weight=1)

    slovo = f'{wordsvoe}'

    global frame
    frame = tk.Frame(window, bg='#6A5ACD')
    frame.grid(row=11, column=0, columnspan=3, pady=20,  sticky="s")
    window.grid_rowconfigure(11, weight=1)
    window.grid_columnconfigure(0, weight=1)

    home.place(x=100, relx=0.015, rely=0.02, anchor='nw')

    helpp = tk.Button(window, text='Помощь', command=lambda: helping(wordsvoe, letters, 1))
    helpp.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')

    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'
    global opened_letters
    opened_letters = ['_' for _ in range(len(wordsvoe))]
    # Создаем полоски, равное кол-ву букв в слове
    labels = []
    for i in range(len(wordsvoe)):
        label = tk.Label(frame, text='_', font=('Arial', 20), fg='white', bg='#6A5ACD')
        label.grid(row=0, column=i, padx=5, pady=5)
        labels.append(label)

    buttons = []
    yellow_indexes = random.sample(range(len(letters)), 3)  # выбираем 3 рандомных индекса
    for i, letter in enumerate(letters):
        bg_color = '#FAEBD7'  # цвет кнопки по умолчанию
        if i in yellow_indexes:
            bg_color = 'yellow'  # цвет кнопки для желтых букв
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
                global lifes
                lifes -= 1
                draw(lifes)
            else:
                btn.config(state=tk.DISABLED)
                btn.config(bg='red')

        btn.config(command=highlight_letter)

def start_chtoto(dif, n):
    nachalo()
    global mem, slovo, tema, labels, helpp, buttons
    Thread(target=next, daemon=True).start()
    mem = f'{nazvanie}'
    tema = tk.Label(font=('Arial', 20), text=f'{nazvanie}', foreground='white', bg='#6A5ACD')
    tema.grid(row=0, column=0, pady=60, padx=20, sticky="nw")
    window.grid_columnconfigure(0, weight=1)

    def random_line(filename):
        with open(filename, encoding='utf-8') as f:
            return random.choice(f.readlines()).strip()

    line = random_line(f'txt\{temma}')
    word = random.choice(line.split()).upper()
    print(word)
    slovo = f'{word}'

    global frame
    frame = tk.Frame(window, bg='#6A5ACD')
    frame.grid(row=11, column=0, columnspan=3, pady=20,  sticky="s")
    window.grid_rowconfigure(11, weight=1)
    window.grid_columnconfigure(0, weight=1)

    home.place(x=100, relx=0.015, rely=0.02, anchor='nw')

    if n != 0:
        helpp = tk.Button(window, text='Помощь', command=lambda: helping(word, letters, n))
        helpp.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')
    else:
        helpp = tk.Button(window, text='Помощь')
        helpp.place(y=100, x=15, relx=0.005, rely=0.02, anchor='nw')
        helpp.config(state=tk.DISABLED)

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
                global lifes
                lifes -= 1
                draw(lifes)
            else:
                btn.config(state=tk.DISABLED)
                btn.config(bg='red')

        btn.config(command=highlight_letter)


#окно игры,
window = tk.Tk()
window.wm_minsize(1200, 600)

lifes = 7

window.title('Hangman')

window.iconphoto(True, tk.PhotoImage(file="pictures\hangman.png"))

window["bg"] = '#6A5ACD'

window.geometry('1350x700')

canvas = Canvas(window, bg='#6A5ACD', height=700, width=1350, highlightthickness=0)
canvas.place(x=0, y=0)

photo1 = PhotoImage(file=r"pictures\mute.png")
photo = PhotoImage(file=r"pictures\audio-speaker-on.png")
photo2 = PhotoImage(file=r'pictures\home-icon-silhouette.png')
photo3 = PhotoImage(file=r'pictures\question.png')
photo4 = PhotoImage(file=r'pictures\simple.png').subsample(12)
photo5 = PhotoImage(file=r'pictures\normal.png').subsample(12)
photo6 = PhotoImage(file=r'pictures\hard.png').subsample(12)
photo7 = PhotoImage(file=r'pictures\).png').subsample(12)
photo8 = PhotoImage(file=r'pictures\super_hard.png').subsample(12)

nn = 0
dif0 = tk.Button(image=photo4, text='Очень легко\n(Бесконечное открытие букв)', compound=RIGHT,
                 bg='#1E90FF', font='Arial 20',
                 command=lambda: start_chtoto(0, 999), width=950)

dif1 = tk.Button(image=photo7, text='Легко\n(5 бесплатных букв, 2 открытие буквы)', compound=RIGHT, bg='#008000',
                 font='Arial 20', command=lambda: start_chtoto(5, 2), width=950)

dif2 = tk.Button(image=photo5, text='Нормально\n(3 бесплатные буквы, 1 открытие буквы)', compound=RIGHT, bg='#ffff40',
                 font='Arial 20', command=lambda: start_chtoto(3, 1), width=950)

dif3 = tk.Button(image=photo6, text='Сложно\n(1 открытие буквы)', compound=RIGHT, bg='#DC143C', font='Arial 20',
                 command=lambda: start_chtoto(0, 1), width=950)

dif4 = tk.Button(image=photo8, text='Очень сложно\n(Нет помощи)', compound=RIGHT, bg='#8B0000', font='Arial 20',
                 command=lambda: start_chtoto(0, 0), width=950)

dif0.grid_forget()
dif1.grid_forget()
dif2.grid_forget()
dif3.grid_forget()
dif4.grid_forget()

ph = tk.Button(image=photo, bg='#FAEBD7', command=sound)
ph.place_forget()

ph1 = tk.Button(image=photo1, bg='#FAEBD7', command=msound)

ph1.place_forget()

ph2 = tk.Button(image=photo3, bg='#FAEBD7')
ph2.bind("<Enter>", pravila)
ph2.bind("<Leave>", leave_message)
ph2.place_forget()

home = tk.Button(text='Сменить тему', image=photo2, compound=LEFT, command=restart_programhome)

home.place_forget()

image = tk.PhotoImage(file=r"pictures\man.png").subsample(3)

foto = Label(window, image=image, bg='#6A5ACD')
foto.place_forget()

window.protocol("WM_DELETE_WINDOW", on_closing)

menu()

window.mainloop()
