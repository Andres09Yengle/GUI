'''
Andres Yengle
11-2
Guis

'''

from tkinter import *
import random
from PIL import Image
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

root=Tk()


#tkinter window
root.geometry("400x400")
#image grab
def select_files():
    global my_image
    filetypes = (('image files', '*.jpg .png'),('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    loop_img(my_image)

# add the parameter my_image to your function
def loop_img(my_image):
    rows = my_image.size[0]
    cols = my_image.size[1]

# open button
open_button = ttk.Button(root,text='Open Files',command=select_files)
open_button.grid(row=0,column=2)

'''
def get_file():
    global my_image
    filename = input("please give a file name ")
    my_image = Image.open(filename)
'''

def My_image():

    red_slider_val_max= red_slider_max.get()
    green_slider_val_max= green_slider_max.get()
    blue_slider_val_max= blue_slider_max.get()
    red_slider_val_min = red_slider_min.get()
    green_slider_val_min = green_slider_min.get()
    blue_slider_val_min = blue_slider_min.get()

    if blue_slider_val_min > blue_slider_val_max:
        messagebox.showerror("information", "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")

    if red_slider_val_min > red_slider_val_max:
        messagebox.showerror("information", "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")

    if green_slider_val_min > green_slider_val_max:
        messagebox.showerror("information", "Please make sure all RGB minimum values are less then their corresponding RGB maximum values")
    else:
        skip_lines = spin.get()
        skip_lines_int = int(skip_lines)
        skip_pixels = spin_2.get()
        skip_pixels_int = int(skip_pixels)

        rows = my_image.size[0]
        cols = my_image.size[1]
        print(rows, cols)

        px = my_image.load()
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

        my_image.show()


#button

Glitch_it = Button(root, text='Glitch it', command=My_image)
Glitch_it.grid(row=0,column=1)
#rgb sliders

red_slider_max = Scale(root, from_=0, to_=255,orient=HORIZONTAL, background='red', fg='grey')
red_slider_max.grid(row=1, column= 1)
green_slider_max = Scale(root, from_=0, to_=255, orient=HORIZONTAL,  background='green', fg='grey')
green_slider_max.grid(row=1, column= 2)
blue_slider_max = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='blue', fg='grey')
blue_slider_max.grid(row= 1, column=3)

red_slider_min = Scale(root, from_=0, to_=255,orient=HORIZONTAL, background='red', fg='grey')
red_slider_min.grid(row=2, column= 1)
green_slider_min = Scale(root, from_=0, to_=255, orient=HORIZONTAL,  background='green', fg='grey')
green_slider_min.grid(row=2, column= 2)
blue_slider_min = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='blue', fg='grey')
blue_slider_min.grid(row= 2, column=3)



#label

max_label = Label(root, text ='Max RGB')
max_label.grid(row=1, column=0)

min_label = Label(root, text = "Min RGB")
min_label.grid(row=2, column=0)

#spinboxes

spin = Spinbox(root, from_=1, to=10, width=3)
spin.grid(row= 3, column=1)
spin_2 = Spinbox(root, from_=0, to=10, width=3)
spin_2.grid(row= 3, column=2)



root.mainloop()