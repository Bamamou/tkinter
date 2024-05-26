from tkinter import *        # to get the GUI module of Pyhton
from pytube import YouTube   #  To get the youtube moule
from tkinter import filedialog  # To get the file dialogue in order to save, open, read files.

window = Tk()
window.title("Pytube")
window.iconphoto(True, PhotoImage(file='RedRose.png'))   # Icon of the window
SAVE_PATH = "C:/Users/admin/OneDrive/Desktop/video"    # Choose where to save your vidoe or audio file

def download(requirement):
    
    video_url = entry.get()  # it allows the ebtry to get the video url
    try: 
        # object creation using YouTube 
        yt =YouTube(video_url)
    except: 
        #to handle exception 
        print("Connection Error") 
    
    # downloading the video 
    try:
        if requirement == "Highest":
            stream = yt.streams.get_highest_resolution()
        elif requirement == "Medium":
            stream = yt.streams.filter(res="360p").first()
        elif requirement == "Lowest":
            stream = yt.streams.get_lowest_resolution()
        elif requirement == "Audio":
            stream = yt.streams.get_audio_only()
    except: 
        print("Some Error!")
    print('Downloading video: ' + yt.streams[0].title)
    stream.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
    
Highest_resolution = Label(window, text ="Copy and paste the video url here", font=('times new roman', 10, 'italic'))
entry = Entry(window, 
              width=50, 
              bg="green", 
              fg="white",
              borderwidth=5,
              font=('times new roman', 15, 'bold')
              )
entry.insert(0, "copy and paste the link of the video here")
#_________________________ Buttons______________________________________________
Highest_resolution_button = Button(window,
                    text="High quality video",
                    command = lambda: download("Highest"),
                    font=('times new roman', 12, 'bold'))
Medium_resolution_button = Button(window,
                    text=" Medium quality video",
                    command = lambda: download("Medium"),
                    font=('times new roman', 12, 'bold'))
Lowest_resolution_button = Button(window,
                    text="Low quality video",
                    command = lambda: download("Lowest"),
                    font=('times new roman', 12, 'bold'))
Audio_button = Button(window,
                    text="Audio",
                    command = lambda: download("Audio"),
                    font=('times new roman', 12, 'bold'))
#______________________display____________________________________________________
Highest_resolution.grid(row=5, column=1)
entry.grid(row=5, column=2, columnspan=4)
Highest_resolution_button.grid(row=6, column=1)
Medium_resolution_button.grid(row=6, column=2)
Lowest_resolution_button.grid(row=6, column=3)
Audio_button.grid(row=6, column=4)

window.mainloop()