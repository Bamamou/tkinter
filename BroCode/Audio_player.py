from tkinter import * 
from tkinter import filedialog, ttk
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title('Music Player')
        self.master.geometry('300x150')
        self.master.iconphoto(True, PhotoImage(file='C:/Users/admin/OneDrive/Desktop/Python/tkinter/BroCode/player.png'))
        
        pygame.init()
        pygame.mixer.init()
        
        self.status = Label(master, text='Select Music', relief=SUNKEN, anchor=W)
        self.status.pack(fill=BOTH, expand=True)

        consumtionbar =  ttk.Progressbar(master, length=100)
        consumtionbar.pack(fill=X)
        
        
        btn_load = Button(master, text='Load Music', command=self.load_music)
        btn_load.pack(fill=X)
        
        btn_play = Button(master, text='Play', command=self.play_music)
        btn_play.pack(fill=X)
        
        btn_pause = Button(master, text='Pause', command=self.pause_music)
        btn_pause.pack(fill=X)

        btn_stop = Button(master, text='Unpause', command=self.unpause_music)
        btn_stop.pack(fill=X)
        
        btn_stop = Button(master, text='Stop', command=self.stop_music)
        btn_stop.pack(fill=X)
      
    print(pygame.mixer.music.get_length())

    def load_music(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            pygame.mixer.music.load(file_path)
            self.status['text'] = 'Music added successfully'
    
    def play_music(self):
        pygame.mixer.music.play()
        self.status['text'] = 'Playing'
    
    def unpause_music(self):
        pygame.mixer.music.unpause()
        self.status['text'] = 'Music Unpaused'
    
    def pause_music(self):
        pygame.mixer.music.pause()
        self.status['text'] = 'Music Paused'
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.status['text'] = 'Music Stopped'

window = Tk()
app = MusicPlayer(window)
window.mainloop()