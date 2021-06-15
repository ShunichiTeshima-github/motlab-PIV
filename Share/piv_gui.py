from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import cv2

class Gui:
    def __init__(self):
        self.execution = False
        logo = cv2.imread('./Share/motlab_nerv.png', -1)
        self.imagewindow = logo

    def lunch(self):
        conf = pd.read_table('./Share/conf.txt', sep=' ', header=None)
        root = Tk()
        root.title('Motlab PIV')

        def show_image():
            dir = entry1.get() + entry2.get()
            num = int(entry2_1.get())
            img = cv2.imread(dir %num, 0)
            self.imagewindow = img
            image_pil = Image.fromarray(img)
            image_tk  = ImageTk.PhotoImage(image_pil)
            image_window = Label(image=image_tk)
            image_window.grid(row=0, column=4, rowspan=11)
            root.mainloop()

        """Image window"""
        image_pil = Image.fromarray(self.imagewindow)
        image_tk  = ImageTk.PhotoImage(image_pil)
        image_window = Label(image=image_tk)
        image_window.grid(row=0, column=4, rowspan=11)

        """Infomation of image file"""
        label1 = Label(root, text='Directory of particle images')
        entry1 = Entry(root)
        entry1.insert(0, conf.loc[0][1])
        label2 = Label(root, text='Image File(name, start number, end number)')
        entry2 = Entry(root)
        entry2.insert(0, conf.loc[1][1])
        entry2_1 = Entry(root)
        entry2_1.insert(0, conf.loc[1][2])
        entry2_2 = Entry(root)
        entry2_2.insert(0, conf.loc[1][3])
        button_show_image = Button(root, text='show image', padx=39, pady=20, command=show_image)

        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        entry2_1.grid(row=1, column=2)
        entry2_2.grid(row=1, column=3)
        button_show_image.grid(row=2, column=0, columnspan=4)

        root.mainloop()

        return self.execution
