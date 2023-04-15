from playsound import playsound

#звук неотгаданной буквы
def play():
    playsound("music\mimi.mp3")

#звук отгаданной буквы
def playgood():
    playsound("music\momo.mp3")

#звук выйгрыша
def win_play():
    playsound("music\win.mp3")

#звук проигрыша
def lose_play():
    playsound("music\lose.mp3")

def back():
    playsound("music\939c0e9b9725e84.mp3")

def next():
    playsound("music\mext.mp3")
