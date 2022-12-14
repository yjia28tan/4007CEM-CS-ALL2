import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
import tkinter.font as tkFont
import customtkinter
customtkinter.set_appearance_mode("dark")


# Create Database
connect = sqlite3.connect('Iccountant.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name       VARCHAR NOT NULL,
    username   VARCHAR NOT NULL,
    email      VARCHAR NOT NULL,
    password   VARCHAR NOT NULL);''')
connect.commit()


class LoginPage(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720')
        self.root.resizable(None, None)
        self.root.title("Iccountant Money Management System")
        self.root.config(bg='black')
        self.lgn_frame = tk.Frame.__init__(self, root)
        self.logo_frame = tk.Frame.__init__(self, root)

        # import picture
        self.logo = ImageTk.PhotoImage(Image.open("logo_refined.png").resize((500, 381), resample=Image.LANCZOS))
        self.logo1 = Label(self.logo_frame, image=self.logo, bg='black')
        self.logo1.pack(side=tk.LEFT, padx=20)

        # title
        tk.Label(self.lgn_frame, text='', bg='black').pack(pady=60)
        self.lgn_title = tk.Label(self.lgn_frame, text='Log In', fg='white', bg='black')
        self.lgn_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.lgn_title.pack(pady=20)
        tk.Label(self.lgn_frame, text='', bg='black').pack(pady=10)

        # email/username
        self.username_or_email_lb = tk.Label(self.lgn_frame, text='Email/username', fg='white', bg='black')
        self.username_or_email_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.username_or_email_lb.pack(pady=5)
        self.username_or_email = StringVar()
        self.username_or_email_entry = Entry(self.lgn_frame, justify='center', width=30, highlightthickness=0,
                                             textvariable=self.username_or_email, relief=FLAT, fg='white', bg='black',
                                             insertbackground='white')
        self.username_or_email_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.username_or_email_entry.pack(pady=5)
        self.username_or_email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.username_or_email_line.pack()

        # password
        self.password_lb = tk.Label(self.lgn_frame, text='Password', fg='white', bg='black')
        self.password_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.password_lb.pack(pady=5)
        self.password = StringVar()
        self.password_lb_entry = Entry(self.lgn_frame, justify='center', width=30, highlightthickness=0,
                                       textvariable=self.password, relief=FLAT, fg='white', bg='black',
                                       insertbackground='white', show='*')
        self.password_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.password_lb_entry.pack(pady=5)
        self.password_lb_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.password_lb_line.pack()
        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.lgn_frame, text='Show password', variable=self.btn_value,
                                     command=self.show_password, fg='white', bg='black')
        self.check_btn.pack(pady=5)

        # import button
        self.lgnbtn = customtkinter.CTkButton(master=self.lgn_frame, text="Login", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190", command=self.data_validation)
        self.lgnbtn.pack(pady=5)

        # register
        self.regbtn = customtkinter.CTkButton(master=self.lgn_frame, text="Register", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190", command=self.open_register)
        self.regbtn.pack(pady=5)

        # forgot password
        self.fgpbtn = customtkinter.CTkButton(master=self.lgn_frame, text="Forgot Password?", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190", command=self.open_forgotpwd)
        self.fgpbtn.pack(pady=5)

    def show_password(self):
        if self.btn_value.get() == 1:
            self.password_lb_entry.config(show='')

        else:
            self.password_lb_entry.config(show='*')

    def data_validation(self):
        self.uname_email = self.username_or_email.get()
        self.pwd = self.password.get()

        # applying empty validation
        if not self.uname_email or not self.pwd:
            messagebox.showerror('Error!', "Please fill the form!")
        else:
            # fetch with username
            cur = connect.execute('SELECT * from user where username="%s"  and password="%s"' % (self.uname_email,
                                                                                                 self.pwd))
            if cur.fetchone():
                messagebox.showinfo('Success!', "Login Success!")
                cur = connect.execute(
                    'SELECT user_id from user WHERE username ="%s" and password="%s"' % (self.uname_email, self.pwd))
                user_id = cur.fetchone()
                userID = user_id
                user_ID = userID
                userid = user_ID[0]
            else:
                # fetch with email
                cur = connect.execute('SELECT * from user where email="%s" and password="%s"' % (self.uname_email,
                                                                                                 self.pwd))
                if cur.fetchone():
                    messagebox.showinfo('Success!', "Login Success!")
                    cur = connect.execute('SELECT user_id from user WHERE email="%s" and password="%s"' %
                                          (self.uname_email, self.pwd))
                    user_id = cur.fetchone()
                    userID = user_id
                    user_ID = userID
                    userid = user_ID[0]
                else:
                    messagebox.showerror('Error!', "Incorrect email, username, or password!")

    def open_register(self):
        self.root.destroy()
        os.system('register.py')

    def open_forgotpwd(self):
        self.root.destroy()
        os.system('Forgotpassword.py')


def main(): 
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()
