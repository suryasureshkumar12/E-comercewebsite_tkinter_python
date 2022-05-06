from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import pymysql
import os
from datetime import datetime
root=Tk()
root.title("Protego.in")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1380,height=100)

name=Label(Heading,
         text="Protego Eyewear",
         fg = "blue",
         bg = "white",
         font = "Helvetica 25 bold italic").grid(row=0,column=2,padx=400)


image_logo=p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/logo1.jpg"))

name=Label(Heading,text="Protego",font="arial 20 bold italic",bg="light pink",fg="blue").grid(row=0,column=1)
# tagline=Label(Heading,text="Wear our Trend!",font="magneto 16 italic",fg="gold",bg="black").grid(row=0,column=2,padx=400)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=250,y=100)
# label_enjoy=Label(Products_frame,text="Wear our Trend!!..",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=480)


#Create an object of tkinter ImageTk

eyeglass1_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/eyeglass_1.jpg"))
eyeglass2_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/eyeglass_2.jpg"))
eyeglass3_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/eyeglass_3.jpg"))
eyeglass4_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/eyeglass_4.jpg"))
eyeglass5_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/eyeglass_5.jpg"))
computerglass1_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/computerglass_1.jpg"))
computerglass2_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/computerglass_2.jpg"))
computerglass3_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/computerglass_3.jpg"))
computerglass4_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/computerglass_4.jpg"))
computerglass5_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/computerglass_5.jpg"))
kidsglass1_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/kidsglass_1.jpg"))
kidsglass2_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/kidsglass_2.jpg"))
kidsglass3_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/kidsglass_3.jpg"))
kidsglass4_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/kidsglass_4.jpg"))
kidsglass5_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/kidsglass_5.jpg"))
sunglass1_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/sunglass_1.jpg"))
sunglass2_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/sunglass_2.jpg"))
sunglass3_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/sunglass_3.jpg"))
sunglass4_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/sunglass_4.jpg"))
sunglass5_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/sunglass_5.jpg"))
readingglass1_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/readingglass_1.jpg"))
readingglass2_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/readingglass_2.jpg"))
readingglass3_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/readingglass_3.jpg"))
readingglass4_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/readingglass_4.jpg"))
readingglass5_image=ptk.PhotoImage(p.Image.open("C:/Users/User1/OneDrive/Desktop/EyewearProject/readingglass_5.jpg"))

#Eyeglassvariables
clicked_eyeglass1 = StringVar()
clicked_eyeglass1.set("Powered Lenses - Rs.1199")
clicked_eyeglass2 = StringVar()
clicked_eyeglass2.set("Premium Lenses - Rs.3000")
clicked_eyeglass3 = StringVar()
clicked_eyeglass3.set("Light Weight Lenses - Rs.1499")
clicked_eyeglass4 = StringVar()
clicked_eyeglass4.set("Frameless Lenses - Rs.899")
clicked_eyeglass5 = StringVar()
clicked_eyeglass5.set("Half-Frame Lenses - Rs.799")
eyeglass_list=[]

#Computerglass variables
clicked_computerglass1 = StringVar()
clicked_computerglass1.set("Powered Lenses - Rs.2199")
clicked_computerglass2 = StringVar()
clicked_computerglass2.set("Premium Lenses - Rs.4000")
clicked_computerglass3 = StringVar()
clicked_computerglass3.set("Light Weight Lenses - Rs.2499")
clicked_computerglass4 = StringVar()
clicked_computerglass4.set("Frameless Lenses - Rs.999")
clicked_computerglass1 = StringVar()
clicked_computerglass1.set("Half-Frame LensesLenses - Rs.1099")
computerglass_list=[]

#kidsglass
clicked_kidsglass1 = StringVar()
clicked_kidsglass1.set("Powered Lenses - Rs.2199")
clicked_kidsglass2 = StringVar()
clicked_kidsglass2.set("Premium Lenses - Rs.1199")
clicked_kidsglass3 = StringVar()
clicked_kidsglass3.set("Light Weight Lenses - Rs.1999")
clicked_kidsglass4 = StringVar()
clicked_kidsglass4.set("Frameless Lenses  - Rs.999")
clicked_kidsglass5= StringVar()
clicked_kidsglass5.set("Half-Frame Lenses - Rs.1099")
kidsglass_list=[]

#sunglass
clicked_sunglass1 = StringVar()
clicked_sunglass1.set("Powered Lenses - Rs.2199")
clicked_sunglass2 = StringVar()
clicked_sunglass2.set("Premium Lenses - Rs.4000")
clicked_sunglass3 = StringVar()
clicked_sunglass3.set("Light Weight Lenses - Rs.1300")
clicked_sunglass4 = StringVar()
clicked_sunglass4.set("Frameless Lenses- Rs.4100")
clicked_sunglass5 = StringVar()
clicked_sunglass5.set("Half-Frame Lenses - Rs.3300")
sunglass_list=[]

#readingglass
clicked_readingglass1 = StringVar()
clicked_readingglass1.set("Powered Lenses - Rs.1199")
clicked_readingglass2 = StringVar()
clicked_readingglass2.set("Premium Lenses  - Rs.3199")
clicked_readingglass3 = StringVar()
clicked_readingglass3.set("Light Weight Lenses  - Rs.2199")
clicked_readingglass4 = StringVar()
clicked_readingglass4.set("Frameless Lenses- - Rs.1199")
clicked_readingglass5 = StringVar()
clicked_readingglass5.set("Half-Frame Lenses- - Rs.999")
readingglass_list=[]

def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")

def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s

# def Products():
def eyeglassCall():
    HideAllFrames()
    eyeglass_label=Label(Products_frame,text="Eyeglasses",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_eyeglass1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_eyeglass1.place(x=10,y=25,width=180,height=280)
    lf_eyeglass2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_eyeglass2.place(x=210,y=35,width=180,height=280)
    lf_eyeglass3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_eyeglass3.place(x=415,y=35,width=180,height=280)
    lf_eyeglass4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_eyeglass4.place(x=620,y=35,width=180,height=280)
    lf_eyeglass5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_eyeglass5.place(x=825,y=35,width=180,height=280)
    label_eyeglass_1=Label(lf_eyeglass1,image=eyeglass1_image,bd=2).grid(row=0,column=0)
    label_eyeglass_2=Label(lf_eyeglass2,image=eyeglass2_image,bd=2).grid(row=0,column=0)
    label_eyeglass_3=Label(lf_eyeglass3,image=eyeglass3_image,bd=2).grid(row=0,column=0,padx=13)
    label_eyeglass_4=Label(lf_eyeglass4,image=eyeglass4_image,bd=2).grid(row=0,column=0)
    label_eyeglass_5=Label(lf_eyeglass5,image=eyeglass5_image,bd=2).grid(row=0,column=0)

    name_eyeglass1=Label(lf_eyeglass1,text="Square Glass",font="arial 9").grid(row=1,column=0)
    name_eyeglass2=Label(lf_eyeglass2,text="Oval Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_eyeglass3=Label(lf_eyeglass3,text="Round Glass",font="arial 9",justify="center").grid(row=1,column=0)
    name_eyeglass4=Label(lf_eyeglass4,text="Coloured Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_eyeglass5=Label(lf_eyeglass5,text="Transparent Colour Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)

    price_eyeglass1=Label(lf_eyeglass1,text="Price: Rs.1199",font="arial 9 bold").grid(row=2,column=0)
    price_eyeglass2=Label(lf_eyeglass2,text="Price: Rs.3000",font="arial 9 bold").grid(row=2,column=0)
    price_eyeglass3=Label(lf_eyeglass3,text="Price: Rs.1499",font="arial 9 bold").grid(row=2,column=0)
    price_eyeglass4=Label(lf_eyeglass4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_eyeglass5=Label(lf_eyeglass5,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)

    def AddE1():
        global eyeglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Square glass",1199,"1,199",Spaces(40-len("Square glass"))])
            messagebox.showinfo("Product Status","Square glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Square glass is not added to the cart.")
    def AddE2():
        global eyeglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Oval glass",3000,"3,000",Spaces(40-len("Oval glass"))])
            messagebox.showinfo("Product Status","Oval glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oval glass is not added to the cart.")
    def AddE3():
        global eyeglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Round glass",1499,"1,499",Spaces(40-len("Round glass"))])
            messagebox.showinfo("Product Status","Round glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Round glass is not added to the cart.")
    def AddE4():
        global eyeglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Coloured glass",899,"899",Spaces(40-len("Coloured glass"))])
            messagebox.showinfo("Product Status","Coloured glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coloured glass is not added to the cart.")
    def AddE5():
        global eyeglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Transparent glass",799,"799",Spaces(40-len("Transparent glass"))])
            messagebox.showinfo("Product Status","Transparent glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Transparent  glass is not added to the cart.")

    add_eyeglass1=Button(lf_eyeglass1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE1).place(x=68,y=245)
    add_eyeglass2=Button(lf_eyeglass2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE2).place(x=68,y=245)
    add_eyeglass3=Button(lf_eyeglass3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE3).place(x=68,y=245)
    add_eyeglass4=Button(lf_eyeglass4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE4).place(x=68,y=245)
    add_eyeglass5=Button(lf_eyeglass5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE5).place(x=68,y=245)

Eyeglass_button=Button(Button_frame,text="Eyeglass",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=eyeglassCall)
Eyeglass_button.grid(row=1,column=0,padx=5,pady=5)

#Computer glass
def computerglassCall():
    HideAllFrames()
    computerglass_label=Label(Products_frame,text="Computerglasses",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_computerglass1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_computerglass1.place(x=10,y=25,width=180,height=280)
    lf_computerglass2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_computerglass2.place(x=210,y=35,width=180,height=280)
    lf_computerglass3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_computerglass3.place(x=415,y=35,width=180,height=280)
    lf_computerglass4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_computerglass4.place(x=620,y=35,width=180,height=280)
    lf_computerglass5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_computerglass5.place(x=825,y=35,width=180,height=280)
    label_computerglass_1=Label(lf_computerglass1,image=computerglass1_image,bd=2).grid(row=0,column=0)
    label_computerglass_2=Label(lf_computerglass2,image=computerglass2_image,bd=2).grid(row=0,column=0)
    label_computerglass_3=Label(lf_computerglass3,image=computerglass3_image,bd=2).grid(row=0,column=0,padx=13)
    label_computerglass_4=Label(lf_computerglass4,image=computerglass4_image,bd=2).grid(row=0,column=0)
    label_computerglass_5=Label(lf_computerglass5,image=computerglass5_image,bd=2).grid(row=0,column=0)

    name_computerglass1=Label(lf_computerglass1,text="Square Glass",font="arial 9").grid(row=1,column=0)
    name_computerglass2=Label(lf_computerglass2,text="Oval Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_computerglass3=Label(lf_computerglass3,text="Round Glass",font="arial 9",justify="center").grid(row=1,column=0)
    name_computerglass4=Label(lf_computerglass4,text="Coloured Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_computerglass5=Label(lf_computerglass5,text="Transparent Colour Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)

    price_computerglass1=Label(lf_computerglass1,text="Price: Rs.1199",font="arial 9 bold").grid(row=2,column=0)
    price_computerglass2=Label(lf_computerglass2,text="Price: Rs.3000",font="arial 9 bold").grid(row=2,column=0)
    price_computerglass3=Label(lf_computerglass3,text="Price: Rs.1499",font="arial 9 bold").grid(row=2,column=0)
    price_computerglass4=Label(lf_computerglass4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_computerglass5=Label(lf_computerglass5,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)

    def AddC1():
        global computerglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            eyeglass_list.append(["Square glass",1199,"1,199",Spaces(40-len("Square glass"))])
            messagebox.showinfo("Product Status","Square glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Square glass is not added to the cart.")
    def AddC2():
        global computerglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            computerglass_list.append(["Oval glass",3000,"3,000",Spaces(40-len("Oval glass"))])
            messagebox.showinfo("Product Status","Oval glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oval glass is not added to the cart.")
    def AddC3():
        global computerglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            computerglass_list.append(["Round glass",1499,"1,499",Spaces(40-len("Round glass"))])
            messagebox.showinfo("Product Status","Round glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Round glass is not added to the cart.")
    def AddC4():
        global computerglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            computerglass_list.append(["Coloured glass",899,"899",Spaces(40-len("Coloured glass"))])
            messagebox.showinfo("Product Status","Coloured glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coloured glass is not added to the cart.")
    def AddC5():
        global computerglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            computerglass_list.append(["Transparent glass",799,"799",Spaces(40-len("Transparent glass"))])
            messagebox.showinfo("Product Status","Transparent glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Transparent  glass is not added to the cart.")

    add_computerglass1=Button(lf_computerglass1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddC1).place(x=68,y=245)
    add_computerglass2=Button(lf_computerglass2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddC2).place(x=68,y=245)
    add_computerglass3=Button(lf_computerglass3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddC3).place(x=68,y=245)
    add_computerglass4=Button(lf_computerglass4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddC4).place(x=68,y=245)
    add_computerglass5=Button(lf_computerglass5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddC5).place(x=68,y=245)

Computerglass_button=Button(Button_frame,text="Computerglass",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=computerglassCall)
Computerglass_button.grid(row=2,column=0,padx=5,pady=5)

#kids glass
def kidsglassCall():
    HideAllFrames()
    kidsglass_label=Label(Products_frame,text="Kidsglass",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_kidsglass1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_kidsglass1.place(x=10,y=25,width=180,height=280)
    lf_kidsglass2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_kidsglass2.place(x=210,y=35,width=180,height=280)
    lf_kidsglass3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_kidsglass3.place(x=415,y=35,width=180,height=280)
    lf_kidsglass4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_kidsglass4.place(x=620,y=35,width=180,height=280)
    lf_kidsglass5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_kidsglass5.place(x=825,y=35,width=180,height=280)
    label_kidsglass_1=Label(lf_kidsglass1,image=kidsglass1_image,bd=2).grid(row=0,column=0)
    label_kidsglass_2=Label(lf_kidsglass2,image=kidsglass2_image,bd=2).grid(row=0,column=0)
    label_kidsglass_3=Label(lf_kidsglass3,image=kidsglass3_image,bd=2).grid(row=0,column=0,padx=13)
    label_kidsglass_4=Label(lf_kidsglass4,image=kidsglass4_image,bd=2).grid(row=0,column=0)
    label_kidsglass_5=Label(lf_kidsglass5,image=kidsglass5_image,bd=2).grid(row=0,column=0)

    name_kidsglass1=Label(lf_kidsglass1,text="Square Glass",font="arial 9").grid(row=1,column=0)
    name_kidsglass2=Label(lf_kidsglass2,text="Oval Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_kidsglass3=Label(lf_kidsglass3,text="Round Glass",font="arial 9",justify="center").grid(row=1,column=0)
    name_kidsglass4=Label(lf_kidsglass4,text="Coloured Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_kidsglass5=Label(lf_kidsglass5,text="Transparent Colour Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)

    price_kidsglass1=Label(lf_kidsglass1,text="Price: Rs.1199",font="arial 9 bold").grid(row=2,column=0)
    price_kidsglass2=Label(lf_kidsglass2,text="Price: Rs.3000",font="arial 9 bold").grid(row=2,column=0)
    price_kidsglass3=Label(lf_kidsglass3,text="Price: Rs.1499",font="arial 9 bold").grid(row=2,column=0)
    price_kidsglass4=Label(lf_kidsglass4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_kidsglass5=Label(lf_kidsglass5,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)

    def AddK1():
        global kidsglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            kidsglass_list.append(["Square glass",1199,"1,199",Spaces(40-len("Square glass"))])
            messagebox.showinfo("Product Status","Square glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Square glass is not added to the cart.")
    def AddK2():
        global kidsglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            kidsglass_list.append(["Oval glass",3000,"3,000",Spaces(40-len("Oval glass"))])
            messagebox.showinfo("Product Status","Oval glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oval glass is not added to the cart.")
    def AddK3():
        global kidsglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            kidsglass_list.append(["Round glass",1499,"1,499",Spaces(40-len("Round glass"))])
            messagebox.showinfo("Product Status","Round glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Round glass is not added to the cart.")
    def AddK4():
        global kidsglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            kidsglass_list.append(["Coloured glass",899,"899",Spaces(40-len("Coloured glass"))])
            messagebox.showinfo("Product Status","Coloured glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coloured glass is not added to the cart.")
    def AddK5():
        global kidsglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            kidsglass_list.append(["Transparent glass",799,"799",Spaces(40-len("Transparent glass"))])
            messagebox.showinfo("Product Status","Transparent glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Transparent  glass is not added to the cart.")

    add_kidsglass1=Button(lf_kidsglass1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddK1).place(x=68,y=243)
    add_kidsglass2=Button(lf_kidsglass2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddK2).place(x=68,y=245)
    add_kidsglass3=Button(lf_kidsglass3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddK3).place(x=68,y=245)
    add_kidsglass4=Button(lf_kidsglass4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddK4).place(x=68,y=245)
    add_kidsglass5=Button(lf_kidsglass5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddK5).place(x=68,y=245)

Kidsglass_button=Button(Button_frame,text="Kidsglass",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=kidsglassCall)
Kidsglass_button.grid(row=3,column=0,padx=5,pady=5)

#sun glass
def sunglassCall():
    HideAllFrames()
    sunglasss_label=Label(Products_frame,text="Sunglass",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_sunglass1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sunglass1.place(x=10,y=25,width=180,height=280)
    lf_sunglass2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sunglass2.place(x=210,y=35,width=180,height=280)
    lf_sunglass3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sunglass3.place(x=415,y=35,width=180,height=280)
    lf_sunglass4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sunglass4.place(x=620,y=35,width=180,height=280)
    lf_sunglass5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sunglass5.place(x=825,y=35,width=180,height=280)
    label_sunglass_1=Label(lf_sunglass1,image=sunglass1_image,bd=2).grid(row=0,column=0)
    label_sunglass_2=Label(lf_sunglass2,image=sunglass2_image,bd=2).grid(row=0,column=0)
    label_sunglass_3=Label(lf_sunglass3,image=sunglass3_image,bd=2).grid(row=0,column=0,padx=13)
    label_sunglass_4=Label(lf_sunglass4,image=sunglass4_image,bd=2).grid(row=0,column=0)
    label_sunglass_5=Label(lf_sunglass5,image=sunglass5_image,bd=2).grid(row=0,column=0)

    name_sunglass1=Label(lf_sunglass1,text="Square Glass",font="arial 9").grid(row=1,column=0)
    name_sunglass2=Label(lf_sunglass2,text="Oval Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_sunglass3=Label(lf_sunglass3,text="Round Glass",font="arial 9",justify="center").grid(row=1,column=0)
    name_sunglass4=Label(lf_sunglass4,text="Coloured Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_sunglass5=Label(lf_sunglass5,text="Transparent Colour Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)

    price_sunglass1=Label(lf_sunglass1,text="Price: Rs.1199",font="arial 9 bold").grid(row=2,column=0)
    price_sunglass2=Label(lf_sunglass2,text="Price: Rs.3000",font="arial 9 bold").grid(row=2,column=0)
    price_sunglass3=Label(lf_sunglass3,text="Price: Rs.1499",font="arial 9 bold").grid(row=2,column=0)
    price_sunglass4=Label(lf_sunglass4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_sunglass5=Label(lf_sunglass5,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)

    def AddS1():
        global sunglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sunglass_list.append(["Square glass",1199,"1,199",Spaces(40-len("Square glass"))])
            messagebox.showinfo("Product Status","Square glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Square glass is not added to the cart.")
    def AddS2():
        global sunglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sunglass_list.append(["Oval glass",3000,"3,000",Spaces(40-len("Oval glass"))])
            messagebox.showinfo("Product Status","Oval glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oval glass is not added to the cart.")
    def AddS3():
        global sunglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sunglass_list.append(["Round glass",1499,"1,499",Spaces(40-len("Round glass"))])
            messagebox.showinfo("Product Status","Round glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Round glass is not added to the cart.")
    def AddS4():
        global sunglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sunglass_list.append(["Coloured glass",899,"899",Spaces(40-len("Coloured glass"))])
            messagebox.showinfo("Product Status","Coloured glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coloured glass is not added to the cart.")
    def AddS5():
        global sunglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sunglass_list.append(["Transparent glass",799,"799",Spaces(40-len("Transparent glass"))])
            messagebox.showinfo("Product Status","Transparent glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Transparent  glass is not added to the cart.")

    add_sunglass1=Button(lf_sunglass1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS1).place(x=68,y=243)
    add_sunglass2=Button(lf_sunglass2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS2).place(x=68,y=245)
    add_sunglass3=Button(lf_sunglass3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS3).place(x=68,y=245)
    add_sunglass4=Button(lf_sunglass4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS4).place(x=68,y=245)
    add_sunglass5=Button(lf_sunglass5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS5).place(x=68,y=245)

Sunglass_button=Button(Button_frame,text="Sunglass",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=sunglassCall)
Sunglass_button.grid(row=4,column=0,padx=5,pady=5)

#reading glass
def readingglassCall():
    HideAllFrames()
    readingglass_label=Label(Products_frame,text="Readingglass",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_readingglass1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_readingglass1.place(x=10,y=25,width=180,height=280)
    lf_readingglass2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_readingglass2.place(x=210,y=35,width=180,height=280)
    lf_readingglass3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_readingglass3.place(x=415,y=35,width=180,height=280)
    lf_readingglass4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_readingglass4.place(x=620,y=35,width=180,height=280)
    lf_readingglass5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_readingglass5.place(x=825,y=35,width=180,height=280)
    label_readingglass_1=Label(lf_readingglass1,image=readingglass1_image,bd=2).grid(row=0,column=0)
    label_readingglass_2=Label(lf_readingglass2,image=readingglass2_image,bd=2).grid(row=0,column=0)
    label_readingglass_3=Label(lf_readingglass3,image=readingglass3_image,bd=2).grid(row=0,column=0,padx=13)
    label_readingglass_4=Label(lf_readingglass4,image=readingglass4_image,bd=2).grid(row=0,column=0)
    label_readingglass_5=Label(lf_readingglass5,image=readingglass5_image,bd=2).grid(row=0,column=0)

    name_readingglass1=Label(lf_readingglass1,text="Square Glass",font="arial 9").grid(row=1,column=0)
    name_readingglass2=Label(lf_readingglass2,text="Oval Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_readingglass3=Label(lf_readingglass3,text="Round Glass",font="arial 9",justify="center").grid(row=1,column=0)
    name_readingglass4=Label(lf_readingglass4,text="Coloured Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_readingglass5=Label(lf_readingglass5,text="Transparent Colour Glass",font="arial 9",justify="center").grid(row=1,column=0,padx=9)

    price_readingglass1=Label(lf_readingglass1,text="Price: Rs.1199",font="arial 9 bold").grid(row=2,column=0)
    price_readingglass2=Label(lf_readingglass2,text="Price: Rs.3000",font="arial 9 bold").grid(row=2,column=0)
    price_readingglass3=Label(lf_readingglass3,text="Price: Rs.1499",font="arial 9 bold").grid(row=2,column=0)
    price_readingglass4=Label(lf_readingglass4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_readingglass5=Label(lf_readingglass5,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)

    def AddR1():
        global readingglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            readingglass_list.append(["Square glass",1199,"1,199",Spaces(40-len("Square glass"))])
            messagebox.showinfo("Product Status","Square glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Square glass is not added to the cart.")
    def AddR2():
        global readingglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            readingglass_list.append(["Oval glass",3000,"3,000",Spaces(40-len("Oval glass"))])
            messagebox.showinfo("Product Status","Oval glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oval glass is not added to the cart.")
    def AddR3():
        global readingglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            readingglass_list.append(["Round glass",1499,"1,499",Spaces(40-len("Round glass"))])
            messagebox.showinfo("Product Status","Round glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Round glass is not added to the cart.")
    def AddR4():
        global readingglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            readingglass_list.append(["Coloured glass",899,"899",Spaces(40-len("Coloured glass"))])
            messagebox.showinfo("Product Status","Coloured glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coloured glass is not added to the cart.")
    def AddR5():
        global readingglass_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            readingglass_list.append(["Transparent glass",799,"799",Spaces(40-len("Transparent glass"))])
            messagebox.showinfo("Product Status","Transparent glass is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Transparent  glass is not added to the cart.")

    add_readingglass1=Button(lf_readingglass1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddR1).place(x=68,y=243)
    add_readingglass2=Button(lf_readingglass2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddR2).place(x=68,y=245)
    add_readingglass3=Button(lf_readingglass3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddR3).place(x=68,y=245)
    add_readingglass4=Button(lf_readingglass4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddR4).place(x=68,y=245)
    add_readingglass5=Button(lf_readingglass5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddR5).place(x=68,y=245)

Readingglass_button=Button(Button_frame,text="Readingglass",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=readingglassCall)
Readingglass_button.grid(row=5,column=0,padx=5,pady=5)

Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="green",font="arial 16 bold")
Coupon_frame.place(x=2,y=480,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.2500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.1500)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)

def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        price_eyeglass=0
        price_computerglass=0
        price_kidsglass=0
        price_sunglass=0
        price_readinglass=0
        for i in range(len(eyeglass_list)):
            price_eyeglass+=eyeglass_list[i][1]
        for i in range(len(computerglass_list)):
            price_computerglass+=computerglass_list[i][1]
        for i in range(len(kidsglass_list)):
            price_kidsglass+=kidsglass_list[i][1]
        for i in range(len(sunglass_list)):
            price_sunglass+=sunglass_list[i][1]
        for i in range(len(readingglass_list)):
            price_readinglass+=readingglass_list[i][1]
        total_price=price_eyeglass+price_computerglass+ price_kidsglass+price_sunglass+price_readinglass
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
             discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.2500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.1500",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        def Bill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"Protego\n"+Spaces(90,'*')+"\n")

            if len(eyeglass_list)>0:
                bill_txt_area.insert(END,"Eyeglass(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in eyeglass_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                    bill_txt_area.insert(END,"\nTotal Eyeglass Price : Rs."+str(price_eyeglass+"\n"+Spaces(90,'*')+"\n"))

            if len(computerglass_list)>0:
                bill_txt_area.insert(END,"Computerglass(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in (computerglass_list):
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Computerglass Price : Rs."+str(price_computerglass)+"\n"+Spaces(90,'*')+"\n")
            if len(kidsglass_list)>0:
                bill_txt_area.insert(END,"Kidsglass(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in kidsglass_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Kidsglass Price : Rs."+str(price_kidsglass)+"\n"+Spaces(90,'*')+"\n")
            if len(sunglass_list)>0:
                bill_txt_area.insert(END,"Sunglass(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in sunglass_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Sunglass Price : Rs."+str(price_sunglass)+"\n"+Spaces(90,'*')+"\n")
            if len(readingglass_list)>0:
                bill_txt_area.insert(END,"Readingglass(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in readingglass_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Readingglass Price : Rs."+str(price_readinglass)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.2500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.1500")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.2500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:Bill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.1500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:Bill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:Bill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed ",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.place(x=1150,y=10)

root.mainloop()