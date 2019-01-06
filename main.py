'''Please Visit rohandas28.github.io for more information'''
from PIL import Image, ImageTk
import tkinter
#Importing Photos
image_list = ['1.jpg', '2.jpg','3.jpg']
text_list = ['Code With Harry', 'Rohan Das','Logo']
current = 0

def move(Rd):
    global current, image_list
    if not (0 <= current + Rd < len(image_list)):
        return
    current += Rd
    image = Image.open(image_list[current])
    photo = ImageTk.PhotoImage(image)
    label['text'] = text_list[current]
    label['image'] = photo
    label.photo = photo


root = tkinter.Tk()

label = tkinter.Label(root, compound=tkinter.TOP)
label.pack()

frame = tkinter.Frame(root)
frame.pack()

tkinter.Button(frame, text='Previous picture', command=lambda: move(-1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Next picture', command=lambda: move(+1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Quit', command=root.quit).pack(side=tkinter.LEFT)

move(0)

root.mainloop()