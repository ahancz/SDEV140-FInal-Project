from tkinter import *
from turtle import backward
#python image library

from PIL import ImageTk,Image

root = Tk()
root.title("My first Python image app")
# icon file is .ico
root.iconbitmap("C:/Users/Sixx/OneDrive/Desktop/SDEV140/gui/imgs/code.ico")

#window size
app_width=500
app_height=550

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width /2)
y = (screen_height / 2) - (app_height /2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')



my_img0 = ImageTk.PhotoImage(Image.open("C:/Users/Sixx/OneDrive/Desktop/SDEV140/gui/imgs/science.png"))
my_img1 = Image.open("C:/Users/Sixx/OneDrive/Desktop/SDEV140/gui/imgs/mew.jpg")
my_img2 = Image.open("C:/Users/Sixx/OneDrive/Desktop/SDEV140/gui/imgs/mew2.jpg")
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/Sixx/OneDrive/Desktop/SDEV140/gui/imgs/MSI.jpg"))

#resized
resized = my_img1.resize((500, 305), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(resized)

resize2 = my_img2.resize((450, 300), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(resize2)





imgList = [my_img0, my_img1, my_img2, my_img3]

status = Label(root, text = "Image 1 of " + str(len(imgList)), bd=1, relief=SUNKEN)

my_label = Label(image=my_img0)
# colomnspan for 3 buttons
my_label.place(relx=0.5, rely = 0.5, anchor = CENTER)

# can use global variables when want to do things in this function that work outside function
def forward(imgNum):
    global my_label
    global backButton
    global forwardButton

    # internal function that gets rid of previous image
    my_label.place_forget()
    # new image + 1, defining
    my_label = Label(image = imgList[imgNum - 1])
    forwardButton = Button(root, text=">>", command=lambda: forward(imgNum+1))
    backButton = Button(root, text="<<", command=lambda: back(imgNum - 1))

# disabling button when reaching the last img
    if imgNum == 4:
        forwardButton = Button(root, text = ">>", state=DISABLED)

    # putting the image up
    my_label.place(relx=0.5, rely = 0.5, anchor = CENTER)
    backButton.place(relx=0.3, rely = 0.93, anchor = S)
    forwardButton.place(relx=0.7, rely = 0.93, anchor = S)

    # updaates status bar
    status = Label(root, text = "Image " + str(imgNum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN)
    status.place(relx=1.0, rely = 1.0, anchor = SE)


def back(imgNum):
    global my_label
    global forwardButton
    global backButton

    my_label.place_forget()
    my_label = Label(image = imgList[imgNum - 1])
    forwardButton = Button(root, text=">>", command=lambda: forward(imgNum+1))
    backButton = Button(root, text="<<", command=lambda: back(imgNum - 1))
    
    if imgNum == 0:
        backButton = Button(root, text="<<", state=DISABLED)


    my_label.place(relx=0.5, rely = 0.5, anchor = CENTER)
    backButton.place(relx=0.3, rely = 0.93, anchor = S)
    forwardButton.place(relx=0.7, rely = 0.93, anchor = S)
    
    # updates status bar
    status = Label(root, text = "Image " + str(imgNum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN)
    status.place(relx=1.0, rely = 1.0, anchor = SE)


# anytime want to pass something through button need to use lambda
backButton = Button(root, text = "<<", command = back, state=DISABLED) # when beginning at the first img, dont need the button to do anything so dont need lambda
exitButton = Button(root, text = "Exit", command=root.quit)
forwardButton = Button(root, text = ">>", command=lambda: forward(2))

backButton.place(relx=0.3, rely = 0.93, anchor = S)
exitButton.place(relx=0.5, rely = 0.93, anchor = S)
forwardButton.place(relx=0.7, rely = 0.93, anchor = S)

status.place(relx=1.0, rely = 1.0, anchor = SE)








root.mainloop()
