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

        main_frame = Frame(root, bd=2,)
        main_frame.place(x=10, y=180, width=1510, height=600)

        # left lebel frame
        Left_frame = LabelFrame(main_frame,bd=2,bg='white',relief="ridge",text="Student Details", font=('times new roman' , 12,'bold'))
        Left_frame.place(x=10, y=10, width=740, height=580)

        # image left 
        img_left_frame = Image.open(r"C:\Users\RAJIV\Desktop\ARS Resources\AI ttandance\AI-ttendance-Main\images\AdobeStock_303989091.jpeg")
        img_left_frame = img_left_frame.resize((720,130), resample=Image.LANCZOS)
        self.photoimg_left_frame = ImageTk.PhotoImage(img_left_frame)

        f_lbl = Label(Left_frame, image=self.photoimg_left_frame)
        f_lbl.place(x=5, y=0, width=730, height=130)

        # Current course information
        current_course_frame = LabelFrame(Left_frame,bd=2,bg='white',relief="ridge",text="Current Course Information", font=('times new roman' , 12,'bold'))
        current_course_frame.place(x=5, y=135, width=720, height=130) 
        
        # Dept info
        dept_label = Label(current_course_frame,text="Department", font=('times new roman', 12,'bold'),bg='white')
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo = ttk.Combobox(current_course_frame, font=('times new roman', 12, 'bold'), width=17,state='readonly')
        dept_combo['values'] = ("Select Department", "CSE", "CST", "CEN", "ECE", "EEE", "EIE")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        # Course info
        course_label = Label(current_course_frame,text="Course", font=('times new roman', 12,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=('times new roman', 12, 'bold'), width=17,state='readonly')
        course_combo['values'] = ("Select Course", "Btech", "Mtech", "MSc", "Management", "Law")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)

        # Year info
        year_label = Label(current_course_frame,text="Admission Year", font=('times new roman', 12,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=('times new roman', 12, 'bold'), width=17,state='readonly')
        year_combo['values'] = ("Select Year", "2021", "2022", "2023", "2024","2025","2026","2027","2028","2029","2030","2031","2032")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)

         # Semestrer info
        semester_label = Label(current_course_frame,text="Semester", font=('times new roman', 12,'bold'),bg='white')
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=('times new roman', 12, 'bold'), width=17,state='readonly')
        semester_combo['values'] = ("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=2,pady=10,sticky=W)


        # Class Student information
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg='white',relief="ridge",text="Class Student Information", font=('times new roman' , 12,'bold'))
        class_Student_frame.place(x=5, y=265, width=720, height=285)

        # Student ID
        studentId_label = Label(class_Student_frame,text="StudentID:", font=('times new roman', 13,'bold'),bg='white')
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20, font=('times new roman', 13,'bold'))
        studentID_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame,text="Student Name:", font=('times new roman', 13,'bold'),bg='white')
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        studentName_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        # Class Div %
        class_div_label = Label(class_Student_frame,text="Percentage:", font=('times new roman', 13,'bold'),bg='white')
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        class_div_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)

        # RollNo
        roll_no_label = Label(class_Student_frame,text="Roll No:", font=('times new roman', 13,'bold'),bg='white')
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        roll_no_entry.grid(row=1, column=3, padx=10,pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame,text="Gender:", font=('times new roman', 13,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        gender_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame,text="DOB:", font=('times new roman', 13,'bold'),bg='white')
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        dob_entry.grid(row=2, column=3, padx=10,pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame,text="Email:", font=('times new roman', 13,'bold'),bg='white')
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        email_entry.grid(row=3, column=1, padx=10,pady=5, sticky=W)

        # Phone no
        phone_label = Label(class_Student_frame,text="Phone No:", font=('times new roman', 13,'bold'),bg='white')
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        phone_entry.grid(row=3, column=3, padx=10,pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame,text="Phone No:", font=('times new roman', 13,'bold'),bg='white')
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        address_entry.grid(row=4, column=1, padx=10,pady=5, sticky=W)

        # Faculty Advisor
        teacher_label = Label(class_Student_frame,text="Faculty Advisor:", font=('times new roman', 13,'bold'),bg='white')
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame, width=20, font=('times new roman', 13,'bold'))
        teacher_entry.grid(row=4, column=3, padx=10,pady=5, sticky=W)



        # right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg='white',relief="ridge",text="Student Details", font=('times new roman' , 12,'bold'))
        Right_frame.place(x=760, y=10, width=740, height=580)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Rec_System(root)
    root.mainloop()
