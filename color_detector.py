import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os
import io




root = tk.Tk()
root.title("Color Detector")
root.geometry("800x470+100+100")
root.config(bg="#e4e8eb")
root.resizable(False,False)

def select_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image file", filetype = (('PNG file','*.png'),('JPG file','*.jpg'),('All Files','*.*')))
    with io.open(filename, 'rb') as file:
        img = Image.open(file)
        img = ImageTk.PhotoImage(img)
        lb1.configure(image=img,width=310,height=270)
        lb1.image=img


def Find_color():
    ct = ColorThief(filename)
    pallet = ct.get_palette(color_count=11)
    rgb1 = pallet[0]
    rgb2 = pallet[1]
    rgb3 = pallet[2]
    rgb4 = pallet[3]
    rgb5 = pallet[4]
    rgb6 = pallet[5]
    rgb7 = pallet[6]
    rgb8 = pallet[7]
    rgb9 = pallet[8]
    rgb10 = pallet[9]

    color1 = f"{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2 = f"{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3 = f"{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4 = f"{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5 = f"{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6 = f"{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7 = f"{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8 = f"{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9 = f"{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10 = f"{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"

    Colors.itemconfig(id1, fill = '#' + color1)
    Colors.itemconfig(id2, fill = '#' + color2)
    Colors.itemconfig(id3, fill = '#' + color3)
    Colors.itemconfig(id4, fill = '#' + color4)
    Colors.itemconfig(id5, fill = '#' + color5)

    Colors1.itemconfig(id6, fill = '#' + color6)
    Colors1.itemconfig(id7, fill = '#' + color7)
    Colors1.itemconfig(id8, fill = '#' + color8)
    Colors1.itemconfig(id9, fill = '#' + color9)
    Colors1.itemconfig(id10, fill = '#' + color10)

    hex1.config(text = '#' + color1)
    hex2.config(text = '#' + color2)
    hex3.config(text = '#' + color3)
    hex4.config(text = '#' + color4)
    hex5.config(text = '#' + color5)
    hex6.config(text = '#' + color6)
    hex7.config(text = '#' + color7)
    hex8.config(text = '#' + color8)
    hex9.config(text = '#' + color9)
    hex10.config(text = '#' + color10)



icon_image = PhotoImage(file ="D:\Vs\Cpp\py\Apps\Color_detector\icon.png") #Import your Icon path
root.iconphoto(False,icon_image)

Label(root,width=120,height=10,bg="#4272f9").pack()

frame = Frame(root,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)

logo=PhotoImage(file="D:\Vs\Cpp\py\Apps\Color_detector\logo.png") #import You logo path here
Label(frame,image=logo,bg="#fff").place(x=10,y=10)

Label(frame,text="Color Detector",font="arial 25 bold",bg="white").place(x=100,y=20)


Colors = Canvas(frame,bg="#fff",width=150,height=265,bd=0)
Colors.place(x=20,y=90)

id1 = Colors.create_rectangle((10,10,50,50),fill="#b8255f")
id2 = Colors.create_rectangle((10,50,50,100),fill="#ff8080")
id3 = Colors.create_rectangle((10,100,50,150),fill="#ff8000")
id4 = Colors.create_rectangle((10,150,50,200),fill="#ffd11a")
id5 = Colors.create_rectangle((10,200,50,250),fill="#bbff33")


hex1 = Label(Colors,text="#b8255f",fg="#000",font="arial 14 bold",bg="white")
hex1.place(x=60,y=15)

hex2 = Label(Colors,text="#ff8080",fg="#000",font="arial 14 bold",bg="white")
hex2.place(x=60,y=65)

hex3 = Label(Colors,text="#ff8000",fg="#000",font="arial 14 bold",bg="white")
hex3.place(x=60,y=115)

hex4 = Label(Colors,text="#ffd11a",fg="#000",font="arial 14 bold",bg="white")
hex4.place(x=60,y=165)

hex5 = Label(Colors,text="#bbff33",fg="#000",font="arial 14 bold",bg="white")
hex5.place(x=60,y=215)

#colors canvas 2

Colors1 = Canvas(frame,bg="#fff",width=150,height=265,bd=0)
Colors1.place(x=180,y=90)

id6 = Colors1.create_rectangle((10,10,50,50),fill="#a64dff")
id7 = Colors1.create_rectangle((10,50,50,100),fill="#66ffd9")
id8 = Colors1.create_rectangle((10,100,50,150),fill="#ff4d88")
id9 = Colors1.create_rectangle((10,150,50,200),fill="#995c00")
id10 = Colors1.create_rectangle((10,200,50,250),fill="#000080")


hex6 = Label(Colors1,text="#a64dff",fg="#000",font="arial 14 bold",bg="white")
hex6.place(x=60,y=15)

hex7= Label(Colors1,text="#66ffd9",fg="#000",font="arial 14 bold",bg="white")
hex7.place(x=60,y=65)

hex8 = Label(Colors1,text="#ff4d88",fg="#000",font="arial 14 bold",bg="white")
hex8.place(x=60,y=115)

hex9 = Label(Colors1,text="#995c00",fg="#000",font="arial 14 bold",bg="white")
hex9.place(x=60,y=165)

hex10 = Label(Colors1,text="#000080",fg="#000",font="arial 14 bold",bg="white")
hex10.place(x=60,y=215)

#select Image

selectimage = Frame(frame,width=340,height=350,bg="#d6dee5")
selectimage.place(x=340,y=10)

f=Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lb1 = Label(f,bg="black")
lb1.place(x=0,y=0)

Button(selectimage,text="Select Image",width=12,height=1, font=("arial",14,"bold"),command=select_image).place(x=10,y=300)
Button(selectimage,text="Find Colors",width=12,height=1,font=("arial",14,"bold"),command=Find_color).place(x=176,y=300)




root.mainloop()
