import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

# tkinter name instance
root = Tk()

# setting the windows size
root.geometry("730x300")
root.configure(bg='white')

#lables
box_1_label = Label(root, text='GUIs are so much fun' , font=('calibra', 10, 'bold'))

box_1_label.grid(row=0, column=0)

box_2_label = Label(root, text='Math makes me cry' , font=('calibra', 10, 'bold'))

box_2_label.grid(row=1, column=0)

box_3_label = Label(root, text='Whats your favorite video game?' , font=('calibra', 10, 'bold'))

box_3_label.grid(row=5, column=0)

box_4_label = Label(root, text='Live Laugh Love!', font=('calibra', 10, 'bold'))

box_4_label.grid(row=2, column=0)



#buttons
def pop_up():
    messagebox.showinfo("information", "Warning")

pop_up_btn = Button(root, text='Virus', command=pop_up)
pop_up_btn.grid(row=0, column=1)

random_button_1 = Button(root, text='Cry')
random_button_1.grid(row=1, column=1)

random_button_2 = Button(root, text='Smile')
random_button_2.grid(row=2, column=1)

random_button_3 = Button(root, text='Die')
random_button_3.grid(row=0, column=2)


#radio buttons
#cake_label
def radio_1():
    print("radio 1")

def radio_2():
    print("radio 2")

def radio_3():
    print("radio 3")

def radio_4():
    print("radio 4")

def radio_5():
    print("radio 5")

r = IntVar()
R1 = Radiobutton(root, text="Option 1", value=0, variable=r, command=radio_1)
R1.grid(row=5, column=1)
R2 = Radiobutton(root, text="Option 2", value=1, variable=r, command=radio_2)
R2.grid(row=5, column=2)



a = IntVar()
R1 = Radiobutton(root, text="Option 1", value=0, variable=a, command=radio_3)
R1.grid(row=4, column=1)
R2 = Radiobutton(root, text="Option 2", value=1, variable=a, command=radio_4)
R2.grid(row=4, column=2)
R3 = Radiobutton(root, text="Option 3", value=2, variable=a, command=radio_5)
R3.grid(row=4, column=3)





#Drop down menu
clicked= StringVar()
main_menu = OptionMenu(root, clicked, "Fortnite", "Roblox", "Minecraft", "Call of Duty")
main_menu.grid(row=6, column=0)

#slider
slider_1= Scale(root, from_=-200, to_=200, orient=HORIZONTAL)
slider_1.grid(row=1, column=2)

slider_2= Scale(root, from_=-2000, to_=2000, orient=HORIZONTAL)
slider_2.grid(row=2, column=2)

#spin box
spin_box_1 = Spinbox(root, from_=-10, to=10)
spin_box_1.grid(row=0, column=7)


#check box
def test_fun():
    print("Yay!")
check_box_1 = Checkbutton(root, text='CB1', onvalue=1, offvalue=0,command=test_fun)
check_box_1.grid(row=3, column=0)

check_box_2 = Checkbutton(root, text='CB2', onvalue=1, offvalue=0,command=test_fun)
check_box_2.grid(row=3, column=1)

check_box_3 = Checkbutton(root, text='CB3', onvalue=1, offvalue=0,command=test_fun)
check_box_3.grid(row=3, column=2)

check_box_4 = Checkbutton(root, text='CB4', onvalue=1, offvalue=0,command=test_fun)
check_box_4.grid(row=3, column=3)

#text entry
entry_box_1 = Entry(root, font=('calibra', 10, 'normal'))
entry_box_1.grid(row=0, column=3)

entry_box_2 = Entry(root, font=('calibra', 10, 'normal'))
entry_box_2.grid(row=1, column=3)



# performing an infinite loop
# for the window to display
root.mainloop()