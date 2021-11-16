'''
Andres Yengle
11-2
Guis

'''

from tkinter import *
import random
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageDraw
import modules_for_advanced_GUI

root = Tk()

# tkinter window
root.geometry("400x400")

'''
# image grab
def select_files():
    global my_image
    global filename
    filetypes = (('image files', '*.jpg .png'), ('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    loop_img(my_image)
'''
def catch():
    print("catch")
    global filename
    filename = modules_for_advanced_GUI.select_files()

def new_filename():
    newfilename = modules_for_advanced_GUI.new_file()
    messagebox.showinfo("information", newfilename)

# add the parameter my_image to your function
def loop_img():
    global size
    global im_resized
    my_image = Image.open(filename)
    im_resized = my_image.resize(size, Image.ANTIALIAS)
    #im_resized.show()
    #return im_resized


# open button
open_button = ttk.Button(root, text='Open Files', command=catch)
open_button.grid(row=0, column=2)


img_size_button = Button(root, text='filename', command= new_filename)
img_size_button.grid(row=6,column=0)


res = ttk.Button(root, text='Change resolution', command=loop_img)
res.grid(row=5, column=0)



def radio_1():
    global size
    size = 256, 144
def radio_2():
    global size
    size = 320, 240
def radio_3():
    global size
    size = 480, 360
def radio_4():
    global size
    size = 852, 480
def radio_5():
    global size
    size = 1280, 720
def radio_6():
    global size
    size = 1920, 1080

R1 = Radiobutton(root, text="144p", value=0, command=radio_1)
R1.grid(row=5, column=1)
R2 = Radiobutton(root, text="240p", value=1, command=radio_2)
R2.grid(row=5, column=2)
R3 = Radiobutton(root, text="360p", value=2, command=radio_3)
R3.grid(row=5, column=3)
R4 = Radiobutton(root, text="480p", value=3, command=radio_4)
R4.grid(row=5, column=4)
R5 = Radiobutton(root, text="720p", value=4, command=radio_5)
R5.grid(row=5, column=5)
R6 = Radiobutton(root, text="1080p", value=5, command=radio_6)
R6.grid(row=5, column=6)


def My_image():
    red_slider_val_max = red_slider_max.get()
    green_slider_val_max = green_slider_max.get()
    blue_slider_val_max = blue_slider_max.get()
    red_slider_val_min = red_slider_min.get()
    green_slider_val_min = green_slider_min.get()
    blue_slider_val_min = blue_slider_min.get()

    if blue_slider_val_min > blue_slider_val_max:
        messagebox.showerror("information",
                             "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")

    if red_slider_val_min > red_slider_val_max:
        messagebox.showerror("information",
                             "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")

    if green_slider_val_min > green_slider_val_max:
        messagebox.showerror("information",
                             "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")
    else:
        skip_lines = spin.get()
        skip_lines_int = int(skip_lines)
        skip_pixels = spin_2.get()
        skip_pixels_int = int(skip_pixels)

        rows = im_resized.size[0]
        cols = im_resized.size[1]
        print(rows, cols)

        px = im_resized.load()
        for i in range(0, rows):

            start = random.randint(0, rows)
            end = random.randint(0, cols)
            nub = random.randint(1, 5)

            if i % 2 == 0:
                start = 0
            else:
                start = i

            for j in range(start, cols, skip_lines_int):
                '''
                red_str= red_slider.get()
                red = int(red_str)
                green_str = green_slider.get()
                green = int(green_str)
                blue_str = blue_slider.get()
                blue = int(blue_str)
                '''
                red = random.randint(red_slider_val_min, red_slider_val_max)
                green = random.randint(green_slider_val_min, green_slider_val_max)
                blue = random.randint(blue_slider_val_min, blue_slider_val_max)
                px[i, j] = (red, green, blue)

    im_resized.show()
def add_text():
    draw = ImageDraw.Draw(im_resized)
    draw.text((10, 10), 'GOOF')



# Add text Button
add_text_button = Button(root, text='Goof', command=add_text)
add_text_button.grid(row=4, column=1)
add_text_label = Label(root, text='Add goof here', font=('calibra', 10, 'bold'))
add_text_label.grid(row=4, column=0)


# Glitch button

Glitch_it = Button(root, text='Glitch it', command=My_image)
Glitch_it.grid(row=0, column=1)
# rgb sliders

red_slider_max = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='red', fg='grey')
red_slider_max.grid(row=1, column=1)
green_slider_max = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='green', fg='grey')
green_slider_max.grid(row=1, column=2)
blue_slider_max = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='blue', fg='grey')
blue_slider_max.grid(row=1, column=3)

red_slider_min = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='red', fg='grey')
red_slider_min.grid(row=2, column=1)
green_slider_min = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='green', fg='grey')
green_slider_min.grid(row=2, column=2)
blue_slider_min = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='blue', fg='grey')
blue_slider_min.grid(row=2, column=3)

# label

max_label = Label(root, text='Max RGB')
max_label.grid(row=1, column=0)

min_label = Label(root, text="Min RGB")
min_label.grid(row=2, column=0)

# spinboxes

spin = Spinbox(root, from_=1, to=10, width=3)
spin.grid(row=3, column=1)
spin_2 = Spinbox(root, from_=0, to=10, width=3)
spin_2.grid(row=3, column=2)

root.mainloop()