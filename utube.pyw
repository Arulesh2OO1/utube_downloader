from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name =""
def openLocation():
    global Folder_Name
    Folder_Name =filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please choose folder!!!!!",fg="red")

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)
        if(choice == choices[0]):
            select =yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select =yt.streams.filter(progressive=True).last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste link again!!!!!",fg="red")
    
    select.download(Folder_Name)
    ytdError.config(text="Download Completed Successfully!!!!!",fg="green")


        
        



root = Tk()
root.title("UTube downloader")
root.geometry("350x350")
root.columnconfigure(0,weight=1)
ytdLabel = Label(root,text="Enter the URL of the video",font=("jost",15))
ytdLabel.grid()
ytdEntryVar=StringVar()
ytdEntry =Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()
ytdError =Label(root,text="Paste Correct URL",fg="red",font=("jost",10))
ytdError.grid()
saveLabel=Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()
locationError = Label(root,text="Choose path correctly",fg="red",font=("jost",10))
locationError.grid()
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()
choices =["720p","144p","Only Audio"]
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.grid()
downloadbtn = Button(root,text ="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()
developerLabel = Label(root,text="Developed by P.P.ARULESH",font=("jost",10))
developerLabel.grid()
root.mainloop()