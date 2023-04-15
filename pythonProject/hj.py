from tkinter import Tk, Button

def mute_sound():
    import pycaw.pycaw as pycaw

    def mute_sound():
        sessions = pycaw.AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "explorer.exe":
                volume.SetMute(1, None)

def unmute_sound():
    import pycaw.pycaw as pycaw

    def unmute_sound():
        sessions = pycaw.AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "explorer.exe":
                volume.SetMute(0, None)

root = Tk()
mute_button = Button(root, text="Выключить звук", command=mute_sound)
unmute_button = Button(root, text="Включить звук", command=unmute_sound)
mute_button.pack()
unmute_button.pack()
root.mainloop()
