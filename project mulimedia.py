from tkinter import *
from tkinter import ttk
root = Tk()
root.title("YouTube Downloader")
root.geometry("400x300")

def download_video(resolution):
    from pytube import YouTube
    try:
        yt = YouTube(link_entry.get())
        if resolution == "high":
            yt.streams.get_highest_resolution().download()
        elif resolution == "low":
            yt.streams.get_lowest_resolution().download()
        elif resolution == "audio":
            yt.streams.filter(only_audio=True).first().download()
        ttk.Label(root, text="Download Successful!", foreground="green").pack()
    except:
        ttk.Label(root, text="Invalid Link! Please Try Again", foreground="red").pack()

label_title = Label(root, text="YouTube Downloader", font=("Arial", 16)).pack(pady=10)
link_entry = Entry(root, width=50)
link_entry.pack(pady=10)

btn_high = Button(root, text="High Resolution", bg="red", fg="white", command=lambda: download_video("high")).pack(pady=5)
btn_low = Button(root, text="Low Resolution", bg="gray", fg="white", command=lambda: download_video("low")).pack(pady=5)
btn_audio = Button(root, text="Audio Only", bg="black", fg="white", command=lambda: download_video("audio")).pack(pady=5)

root.mainloop()