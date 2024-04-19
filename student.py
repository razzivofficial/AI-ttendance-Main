from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Rec_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        #image1
        img1 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\face-recognition.png")
        img1 = img1.resize((500,130), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=10, y=0, width=500, height=130)

        #image2
        img2 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((500,130), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=510, y=0, width=510, height=130)

        #image3
        img3 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\smart-attendance.jpg")
        img3 = img3.resize((500,130), resample=Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1020, y=0, width=500, height=130)

        # Background image
        bg_img = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\bg.jpg")
        bg_img = bg_img.resize((1530,710), resample=Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        bg_img_lbl = Label(self.root, image=self.photobg_img)
        bg_img_lbl.place(x=0, y=130, width=1530, height=710)

        #title
        title_lbl=Label(bg_img_lbl, text="STUDENT MANAGEMENT SYSTEM", font=('times new roman' , 35,'bold'),bg='white',fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1530, height=45)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Rec_System(root)
    root.mainloop()
