import tkinter as tk
from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os
#title
global rt
rt=Tk()
rt.title("(Color Finder)")
rt.geometry("800x470+100+100")
rt.configure(bg="#e4e8eb")
rt.resizable(False,False)

def upload_Image():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',filetype=(('PNG file','*.png'),('JPG file','*.jpg'),('ALL file','*.txt')))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lb.configure(image=img,width=310, height=270)
    lb.image=img

def Find_Colors():
    ct=ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    rgb1=palette [0]
    rgb2=palette [1]
    rgb3=palette [2]
    rgb4=palette [3]
    rgb5=palette [4]
    rgb6=palette [5]
    rgb7=palette [6]
    rgb8=palette [7]
    rgb9=palette [8]
    rgb10=palette [9]

    

    color1=f"#{rgb1[0]:02x}{rgb1[1]}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]}{rgb5[2]:02x}"
    color6=f"#{rgb6[0]:02x}{rgb6[1]}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]}{rgb10[2]:02x}"

    cr.itemconfig(i1,   fill=color1)
    cr.itemconfig(i2,   fill=color2)
    cr.itemconfig(i3,   fill=color3)
    cr.itemconfig(i4,   fill=color4)
    cr.itemconfig(i5,   fill=color5)

    cr2.itemconfig(i6,   fill=color6)
    cr2.itemconfig(i7,   fill=color7)
    cr2.itemconfig(i8,   fill=color8)
    cr2.itemconfig(i9,   fill=color9)
    cr2.itemconfig(i10,   fill=color10)

    h1.config(text=color1)
    h2.config(text=color2)
    h3.config(text=color3)
    h4.config(text=color4)
    h5.config(text=color5)
    h6.config(text=color6)
    h7.config(text=color7)
    h8.config(text=color8)
    h9.config(text=color9)
    h10.config(text=color10)

    
                                                        

#icon
imicon=PhotoImage(file="icon.png")
rt.iconphoto(False,imicon)


Label(rt,width=120,height=10,bg="#4272f9").pack()

frame=Frame(rt,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)
#logo
lg=PhotoImage(file="logo.png")
Label(frame,image=lg,bg="#fff").place(x=10,y=10)

Label(frame,text="Color Finder",font="arial 25 bold", bg="white").place(x=100,y=20)
#cr1
#iii
#h
#colors

cr=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
cr.place(x=20,y=90)

i1 = cr.create_rectangle((10,10,50,50),fill="#b8255f")
i2 = cr.create_rectangle((10,50,50,100),fill="#db4035")
i3 = cr.create_rectangle((10,100,50,150),fill="#ff9933")
i4 = cr.create_rectangle((10,150,50,200),fill="#fad000")
i5 = cr.create_rectangle((10,200,50,250),fill="#afb83b")

h1=Label(cr,text="#b8255f",fg="#000",font="arial 12 bold",bg="white")
h1.place(x=60,y=15)
h2=Label(cr,text="#db4035",fg="#000",font="arial 12 bold",bg="white")
h2.place(x=60,y=65)
h3=Label(cr,text="#ff9933",fg="#000",font="arial 12 bold",bg="white")
h3.place(x=60,y=115)
h4=Label(cr,text="#fad000",fg="#000",font="arial 12 bold",bg="white")
h4.place(x=60,y=165)
h5=Label(cr,text="#afb83b",fg="#000",font="arial 12 bold",bg="white")
h5.place(x=60,y=215)
#cr2
#ii
#hh
#colors2
cr2=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
cr2.place(x=180,y=90)

i6 = cr2.create_rectangle((10,10,50,50),fill="#7ecc49")
i7 = cr2.create_rectangle((10,50,50,100),fill="#299438")
i8 = cr2.create_rectangle((10,100,50,150),fill="#6accbc")
i9 = cr2.create_rectangle((10,150,50,200),fill="#158fad")
i10 = cr2.create_rectangle((10,200,50,250),fill="#14aaf5")

h6=Label(cr2,text="#7ecc49",fg="#000",font="arial 12 bold",bg="white")
h6.place(x=60,y=15)
h7=Label(cr2,text="#299438",fg="#000",font="arial 12 bold",bg="white")
h7.place(x=60,y=65)
h8=Label(cr2,text="#6accbc",fg="#000",font="arial 12 bold",bg="white")
h8.place(x=60,y=115)
h9=Label(cr2,text="#158fad",fg="#000",font="arial 12 bold",bg="white")
h9.place(x=60,y=165)
h10=Label(cr2,text="#14aaf5",fg="#000",font="arial 12 bold",bg="white")
h10.place(x=60,y=215)




#image selection

select_image=Frame(frame,width=340,height=350,bg="#d6dee5")
select_image.place(x=350,y=10)
f=Frame(select_image,bd=3 ,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lb=Label(f,bg="black")
lb.place(x=0,y=0)

Button(select_image,text="Upload Image",width=12,height=1,font="arial 14 bold",command=upload_Image).place(x=10,y=300)
Button(select_image, text="Find Colors",width=12,height=1,font="arial 14 bold",command=Find_Colors).place(x=176,y=300)




rt.mainloop()









