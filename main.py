from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Rec_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x720+0+0")
        self.root.title("Face Recognition System")
        
        # Background image
        bg_img = Image.open(r"C:\Users\HP\Desktop\Code\face rec project\images\bgimg.png")
        bg_img = bg_img.resize((1360,720), resample=Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        f_lbl = Label(self.root, image=self.photobg_img)
        f_lbl.place(x=0, y=0, width=1360, height=720)

        # Student button
        img1 = Image.open(r"C:\Users\HP\Desktop\Code\face rec project\images\student_img.jpg")
        img1 = img1.resize((200,200), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1)
        b1.place(x=100, y=100, width=200, height=200)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Rec_System(root)
    root.mainloop()
