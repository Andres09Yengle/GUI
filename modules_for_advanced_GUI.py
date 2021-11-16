from tkinter import filedialog as fd
from PIL import Image

def select_files():
    global my_image
    global filename
    filetypes = (('image files', '*.jpg .png'), ('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    #my_image = Image.open(filename)
    #@loop_img(my_image)
    return filename


def new_file():
    global filename
    new_filename = "the name of the file is " + filename
    return new_filename