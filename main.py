import tkinter as tk
from tkinter.filedialog import askdirectory
import vlc
import os


class MusicPlayer:
    def __init__(self):
        self.media_player = vlc.MediaPlayer()
        self.mp = tk.Tk()
        mp = self.mp
        windowWidth = mp.winfo_reqwidth()
        self.windowWidth = windowWidth
        windowHeight = mp.winfo_reqheight()
        positionRight = int(mp.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(mp.winfo_screenheight()/2 - windowHeight/2)

        self.mp.title("♫ Muzique ♫")
        self.mp.geometry("425x300")

    def directorySelector(self):
        directory = askdirectory()
        os.chdir(directory)
        song_list = os.listdir()

        self.playList = tk.Listbox(self.mp, width=int(self.windowWidth*0.2), font="Helvetica 12 bold", bg="red", fg='black', selectmode=tk.SINGLE)
        pos = 0
        for item in song_list:
            self.playList.insert(pos, item)
            pos +=1

    def play(self):
        var = self.playList.get(tk.ACTIVE)
        self.var.set(var[:30]+'....')
        media = vlc.Media(var)
        self.media_player.set_media(media)
        self.media_player.play()


    def stop(self):
        self.media_player.stop()
        self.pauseButton.configure(fg="white")
        self.var.set('Sounds like empty.')

    def pause(self):
        self.media_player.pause()
        if self.status == 'PAUSE':
            self.status='UNPAUSE'
            self.pauseButton.configure(fg="black")
        else:
            self.status='PAUSE'
            self.pauseButton.configure(fg="white")

    def interface(self):
        self.status = "PAUSE"
        self.directorySelector()
        self.buttonframe = tk.Frame(self.mp)
        playButton = tk.Button(self.buttonframe, width=4, height=2, font="Helvetica 16 bold", text="►", command=self.play, bg="blue", fg="white")
        stopButton = tk.Button(self.buttonframe, width=4, height=2, font="Helvetica 16 bold", text="⏹", command=self.stop, bg="red", fg="white")
        self.pauseButton = tk.Button(self.buttonframe, width=4, height=2, font="Helvetica 16 bold", text="⏯️", command=self.pause, bg="purple", fg="white")
        self.var = tk.StringVar()
        self.var.set('Sounds like empty.')
        song_title = tk.Label(self.mp, font="Helvetica 12 bold", textvariable=self.var)
        song_title.grid(row=0, column=1, padx=5,pady=5)

        
        self.buttonframe.grid(row=1, column=0, columnspan=2)  
        playButton.grid(row =0, column=1, padx=1,pady=5)
        stopButton.grid(row=0, column=2, padx=1,pady=5)
        self.pauseButton.grid(row=0, column=3, padx=1,pady=5)
        
        self.playList.grid(row=3, column=1, padx=32, pady=5)

        self.mp.mainloop()

    def startPlayer(self):
        self.interface()


def main():
    player = MusicPlayer()
    player.startPlayer()

if __name__ == "__main__":
    main()