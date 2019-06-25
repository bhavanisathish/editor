# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:05:28 2019

@author: lenovA
"""

import os
from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import askcolor
from tkinter import filedialog

root=Tk()
menub=Menu(root)
text=Text(root,height=70,width=1250,font=("Arial",10),undo=True)
scrbar=Scrollbar(root,command=text.yview,width=15)
scrbar.config(command=text.yview)
text.config(yscrollcommand=scrbar.set)
scrbar.pack(side=RIGHT,fill=Y)
text.pack(expand=YES)
frame=Frame(root,width=20)
frame.pack(expand=NO,fill=Y,side=LEFT)


root.config(menu=menub)
#creating sub menu
def newf():
    root.title("Untitled-np")
    file=NONE
    text.delete(1.0,End)
def browse():
    global fm          #load la place pannu
    fm=filedialog.askopenfilename()
    root.title(os.path.basename(fm))
    if fm:
        text.delete(1.0,END)
        file=open(fm,"r")
        text.insert(1.0,file.read())
    print(fm)

def savefi():
    filename=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=(("All Files","*.*"),("Text Documnets",".txt")))
    if filename:
        file=open(filename,'w')#,encoding="UTF-8")
        alltext=text.get(1.0,END)
        file.write(alltext)
        root.title(os.path.basename(filename))
        file.close()
  
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")
def clear():
    text.delete(SEL_FIRST,SEL_LAST)
def clearall():
    text.delete(1.0,END)
def undo():
    text.event_generate("<<Undo>>")
def redo():
    text.event_generate("<<Redo>>")
def about_us():
    tkinter.messagebox.showinfo('MUSIC','Enjoy the music')
def times():
    global text
    text.config(font="Times")
def courier():
    global text
    text.config(font="Courier")
def hel():
    global text
    text.config(font="Helvetica")
def four():
    global text
    text.config(font=(False,4))
def eight():
    global text
    text.config(font=(False,8))
def twelve():
    global text
    text.config(font=(False,12))
def sixteen():
    global text
    text.config(font=(False,16))
def twenty():
    global text
    text.config(font=(False,20))
def twofour():
    global text
    text.config(font=(False,24))
def twoeight():
    global text
    text.config(font=(False,28))
def threetwo():
    global text
    text.config(font=(False,32))
def sixtyfour():
    global text
    text.config(font=(False,64))
def capi():
    pass
def bold():
    global text
    text.tag_add("bold","sel.first","sel.last")
    text.tag_config("bold",font=("Arial","10","bold"))
def italic():
    global text
    text.tag_add("bold","sel.first","sel.last")
    text.tag_config("bold",font=("Arial","10","italic"))   
def underline():
    global text
    text.tag_add("bold","sel.first","sel.last")
    text.tag_config("bold",font=("Arial","10","underline"))   
def back():
    (triple,color)=askcolor()
    if color:
        global text
        text.config(background=color)
def fore():
    (triple,color)=askcolor()
    if color:
        global text
        text.config(foreground=color)
    
smenu=Menu(menub,tearoff=0)
menub.add_cascade(label="File",menu=smenu)
smenu.add_command(label="New",command=newf)  #cascade
smenu.add_command(label="Open",command=browse)
smenu.add_command(label="save",command=savefi)
smenu.add_command(label="Exit",command=root.destroy)
smenu1=Menu(menub,tearoff=0)
menub.add_cascade(label="edit",menu=smenu1)
smenu1.add_command(label="Cut",command=cut)
smenu1.add_command(label="Copy",command=copy)
smenu1.add_command(label="Paste",command=paste)
smenu1.add_command(label="Clear",command=clear)
smenu1.add_command(label="Clear all",command=clearall)
smenu1.add_command(label="undo",command=text.edit_undo)
smenu1.add_command(label="redo",command=text.edit_redo)
smenu2=Menu(menub,tearoff=0)
menub.add_cascade(label="Help",menu=smenu2)
smenu2.add_command(label="about us",command=about_us)
#font family
ssmenu=Menu(menub,tearoff=0)
menub.add_cascade(label="font",menu=ssmenu)
ssmenu.add_command(label="Times New Roman",command=times)
ssmenu.add_command(label="Courier",command=courier)
ssmenu.add_command(label="Helvetica",command=hel)
#ssmenu.add_command(label="",command=)
#font size
sssmenu=Menu(menub,tearoff=0)
menub.add_cascade(label="Font size",menu=sssmenu)
sssmenu.add_command(label="4",command=four)
sssmenu.add_command(label="8",command=eight)
sssmenu.add_command(label="12",command=twelve)
sssmenu.add_command(label="16",command=sixteen)
sssmenu.add_command(label="20",command=twenty)
sssmenu.add_command(label="24",command=twofour)
sssmenu.add_command(label="28",command=twoeight)
sssmenu.add_command(label="32",command=threetwo)
sssmenu.add_command(label="64",command=sixtyfour)
#font highlight
ssssmenu=Menu(menub,tearoff=0)
menub.add_cascade(label="text attribute",menu=ssssmenu)
ssssmenu.add_command(label="capitalise",command=capi)
ssssmenu.add_command(label="bold",command=bold)
ssssmenu.add_command(label="italic",command=italic)
ssssmenu.add_command(label="underlined",command=underline)
ssssmenu.add_command(label="background color",command=back)
ssssmenu.add_command(label="foreground color",command=fore)

sbar=Label(root,text="fm", relief=SUNKEN,anchor=W)        #play_music sbar["text"]="play"+os.path.basename(fm)
sbar.pack(side=BOTTOM,fill=X)
root.mainloop()



