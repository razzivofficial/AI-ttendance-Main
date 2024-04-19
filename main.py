from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Rec_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        #image1
        img1 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\Stanford.jpg")
        img1 = img1.resize((500,130), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=10, y=0, width=500, height=130)

        #image2
        img2 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\facialrecognition.png")
        img2 = img2.resize((500,130), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=510, y=0, width=510, height=130)

        #image3
        img3 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\u.jpg")
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
        title_lbl=Label(bg_img_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=('times new roman' , 35,'bold'),bg='white',fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        
        # Student button
        img4 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\student_img.jpg")
        img4 = img4.resize((220,220), resample=Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg4, cursor='hand2')
        b1.place(x=220, y=230, width=220, height=220)

        b1_1 = Button(self.root, text="Student Details", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=220, y=430, width=220, height=40)

        # Face Detector
        img5 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\face_detector1.jpg")
        img5 = img5.resize((220,220), resample=Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root, image=self.photoimg5, cursor='hand2')
        b1.place(x=500, y=230, width=220, height=220)

        b1_1 = Button(self.root, text="Face Dector", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=500, y=430, width=220, height=40)

        # Attendance
        img6 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\report.jpg")
        img6 = img6.resize((220,220), resample=Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(self.root, image=self.photoimg6, cursor='hand2')
        b1.place(x=780, y=230, width=220, height=220)

        b1_1 = Button(self.root, text="Attendance", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=780, y=430, width=220, height=40)

        # Help Desk
        img7 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220,220), resample=Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(self.root, image=self.photoimg7, cursor='hand2')
        b1.place(x=1060, y=230, width=220, height=220)

        b1_1 = Button(self.root, text="Help Desk", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=1060, y=430, width=220, height=40)


        # Train Data
        img8 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\Train.jpg")
        img8 = img8.resize((220,220), resample=Image.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1 = Button(self.root, image=self.photoimg8, cursor='hand2')
        b1.place(x=220, y=520, width=220, height=220)

        b1_1 = Button(self.root, text="Train Data", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=220, y=720, width=220, height=40)

        # Photos
        img9 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220,220), resample=Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(self.root, image=self.photoimg9, cursor='hand2')
        b1.place(x=500, y=520, width=220, height=220)

        b1_1 = Button(self.root, text="Photos", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=500, y=720, width=220, height=40)

        # Devloper
        img10 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220,220), resample=Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(self.root, image=self.photoimg10, cursor='hand2')
        b1.place(x=780, y=520, width=220, height=220)

        b1_1 = Button(self.root, text="Developer", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=780, y=720, width=220, height=40)

        # Exit
        img11 = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\exit.jpg")
        img11 = img11.resize((220,220), resample=Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(self.root, image=self.photoimg11, cursor='hand2')
        b1.place(x=1060, y=520, width=220, height=220)

        b1_1 = Button(self.root, text="Exit", cursor='hand2', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white')
        b1_1.place(x=1060, y=720, width=220, height=40)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Rec_System(root)
    root.mainloop()
