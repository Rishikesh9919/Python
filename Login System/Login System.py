from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='login_system'
)

cursor = con.cursor(buffered=True)

root = Tk()
root.geometry('550x450+50+50')
root.maxsize(width=550, height=450)
root.minsize(width=550, height=450)
root.title('Login System')

font = Font(family='Helvetica', size=11)
bigfont = Font(family='Helvetica', size=14, weight='bold')


def Back(labelFrame, anyFrame):
    anyFrame.pack_forget()
    labelFrame.pack(padx=100, pady=60)


def showdetails(labelFrame, mainFrame, data):
    detailFrame = LabelFrame(mainFrame, text=' Details ', font=bigfont)
    detailFrame.pack(padx=80, pady=60)

    idlbl = Label(detailFrame, text='ID: ', font=font)
    idlbl.grid(row=0, column=0, padx=(30, 5), pady=(30, 10), sticky='E')
    id = Label(detailFrame, text=data[0], font=font)
    id.grid(row=0, column=1, padx=(0, 30), pady=(30, 10), sticky='W')

    namelbl = Label(detailFrame, text='Name: ', font=font)
    namelbl.grid(row=1, column=0, padx=(30, 5), sticky='E')
    name = Label(detailFrame, text=data[1], font=font)
    name.grid(row=1, column=1, padx=(0, 30), sticky='W')

    emaillbl = Label(detailFrame, text='E-Mail: ', font=font)
    emaillbl.grid(row=2, column=0, padx=(30, 5), pady=10, sticky='E')
    email = Label(detailFrame, text=data[2], font=font)
    email.grid(row=2, column=1, padx=(0, 30), pady=10, sticky='W')

    password = Label(detailFrame, text='Password: ', font=font)
    password.grid(row=3, column=0, padx=(30, 5), pady=(0, 30), sticky='E')
    password = Label(detailFrame, text=data[3], font=font)
    password.grid(row=3, column=1, padx=(0, 30), pady=(0, 30), sticky='W')

    back = Button(detailFrame, text='Log Out', width=7, height=1, font=font, padx=4, pady=4,
                  command=lambda: Back(labelFrame, detailFrame))
    back.grid(row=4, column=1, padx=(20, 20), pady=(20, 20), sticky='E')


def login(email, password, loginFrame, labelFrame, mainFrame):
    cursor.execute('Select * from login_system')
    for data in cursor:
        if data[2] == email:
            if data[3] == password:
                loginFrame.pack_forget()
                messagebox.showinfo('Login Sucessful', 'Login Successful..!')
                showdetails(labelFrame, mainFrame, data)
                break
            else:
                messagebox.showwarning('Login Failed', 'Login Failed')
    else:
        messagebox.showwarning('Login Failed', 'E-Mail Id Doesn\'t Exist!')


def Add_to_database(name, email, password):
    cursor.execute('Select * from login_system')
    for data in cursor:
        if data[2] == email:
            messagebox.showwarning('Registration Failed', 'Data already Exists..!')
            break
    else:
        cursor.execute('Insert into login_system(Name,Email,Password) values(%s,%s,%s)', (name, email, password))
        con.commit()
        messagebox.showinfo('Registration Sucessful', 'Registration Successful..!')
        cursor.execute('Select * from login_system')
        for data in cursor:
            print(data)


def LoginGUI(mainFrame, labelFrame):
    labelFrame.pack_forget()

    loginFrame = LabelFrame(mainFrame, text=' Login ', font=bigfont)
    loginFrame.pack(padx=80, pady=60)

    emaillbl = Label(loginFrame, text='E-Mail', font=font)
    emaillbl.grid(row=0, column=1, padx=(30, 0), pady=(30, 10), sticky='E')

    emailentry = Entry(loginFrame, font=font, bd=2)
    emailentry.grid(row=0, column=2, padx=(10, 20), pady=(30, 10))

    passwordlbl = Label(loginFrame, text='Password', font=font)
    passwordlbl.grid(row=1, column=1, padx=(30, 0), pady=(30, 10), sticky='E')

    passentry = Entry(loginFrame, font=font, bd=2)
    passentry.grid(row=1, column=2, padx=(10, 20), pady=(30, 10))
    passentry.config(show='*')

    submit = Button(loginFrame, text='Submit', width=10, height=1, font=font, padx=4, pady=4,
                    command=lambda: login(str(emailentry.get()), str(passentry.get()), loginFrame, labelFrame,
                                          mainFrame))
    submit.grid(row=2, column=2, padx=(30, 20), pady=(50, 30), sticky='E')

    back = Button(loginFrame, text='Back', width=7, height=1, font=font, padx=4, pady=4,
                  command=lambda: Back(labelFrame, loginFrame))
    back.grid(row=2, column=1, padx=(20, 30), pady=(50, 30), sticky='W')


def Register(mainFrame, labelFrame):
    labelFrame.pack_forget()

    regFrame = LabelFrame(mainFrame, text=' Register ', font=bigfont)
    regFrame.pack(padx=80, pady=40)

    namelbl = Label(regFrame, text='Name', font=font, pady=10)
    namelbl.grid(row=0, column=1, padx=(30, 0), pady=(30, 0), sticky='E')

    nameentry = Entry(regFrame, font=font, bd=2)
    nameentry.grid(row=0, column=2, padx=(10, 30), pady=(30, 0))

    emaillbl = Label(regFrame, text='E-Mail', font=font)
    emaillbl.grid(row=1, column=1, padx=(30, 0), pady=(30, 10), sticky='E')

    emailentry = Entry(regFrame, font=font, bd=2)
    emailentry.grid(row=1, column=2, padx=(10, 30), pady=(30, 10))

    passwordlbl = Label(regFrame, text='Password', font=font)
    passwordlbl.grid(row=2, column=1, padx=(30, 0), pady=(30, 10), sticky='E')

    passentry = Entry(regFrame, font=font, bd=2)
    passentry.grid(row=2, column=2, padx=(10, 30), pady=(30, 10))

    submit = Button(regFrame, text='Submit', width=10, height=1, font=font, padx=4, pady=4,
                    command=lambda: Add_to_database(str(nameentry.get()), str(emailentry.get()), str(passentry.get())))
    submit.grid(row=3, column=2, padx=(30, 20), pady=(50, 30), sticky='E')

    back = Button(regFrame, text='Back', width=7, height=1, font=font, padx=4, pady=4,
                  command=lambda: Back(labelFrame, regFrame))
    back.grid(row=3, column=1, padx=(20, 30), pady=(50, 30), sticky='W')


def Account(mainFrame):
    labelFrame = LabelFrame(mainFrame, text=' Account ', font=bigfont)
    labelFrame.pack(padx=100, pady=60)

    login = Button(labelFrame, text='Login', width=10, height=1, font=font, padx=4, pady=4,
                   command=lambda: LoginGUI(mainFrame, labelFrame))
    login.pack(padx=100, pady=(40, 20))

    Or = Label(labelFrame, text='or', font=font)
    Or.pack(padx=100)

    register = Button(labelFrame, text='Register', width=10, height=1, font=font, padx=4, pady=4,
                      command=lambda: Register(mainFrame, labelFrame))
    register.pack(padx=100, pady=(20, 40))


mainFrame = Frame(root, height=450, width=550)
mainFrame.pack(fill='both', expand=True)

Account(mainFrame)

mainloop()
