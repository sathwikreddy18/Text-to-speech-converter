from tkinter import *
import pyttsx3
root=Tk()
root.title('Text to Speech Converter')
#p=PhotoImage(file='allotmentorder.JPG')
#root.iconphoto(False,p)
root.geometry('600x500')
def convert():
    eng=pyttsx3.init()
    voices=eng.getProperty('voices')

    eng.setProperty('voice',voices[1].id)
    eng.say(my_entry.get())
    eng.runAndWait()
    my_entry.delete(0,END)
my_entry=Entry(root,font=('Helvatica,28'))
my_entry.pack(pady=20)
b=Button(root,text="Speech",command=convert)
b.pack(pady=20)




root.mainloop()
    
