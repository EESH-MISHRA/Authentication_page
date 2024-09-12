'''tkinter program :- login portal '''
from tkinter import *
from tkinter import PhotoImage
from PIL import Image
from function_signin import *
def login_page():
    root.destroy()
    import login_main # type: ignore



root = Tk()
# Bitmap icon
root.iconbitmap(r'icon.ico')
#title
root.title('Google Sign in ')
#window size
canvas_height = 1080
canvas_width = 720
root.geometry(f'{canvas_height}x{canvas_width}')
root.minsize(canvas_height,canvas_width)
root.maxsize(canvas_height,canvas_width)
#base window
base_window = Canvas(root,height=1080,width=720)
base_window.pack(fill=BOTH)

#base window :- Trinalges 1/2
base_window.create_polygon((0,0,0,720,1080,720),fill='#003366') 
base_window.create_polygon((0,0,1080,0,1080,720),fill='#2C4E72')

#Create a new frame above the login_window
login_window = Frame(root,background='white',highlightbackground='black',highlightthickness=1)
login_window.place(relx=0.5,rely=0.5,anchor='center',height=650,width=540)  # Centered placement
#username label
username_label = Label(login_window,text='Username',font='arial 10 bold',foreground='black',background='white')
username_label.place(x=50,y=300)
#password label
pasword_label = Label(login_window,text='Password',font='arial 10 bold',foreground='black',background='white')
pasword_label.place(x=50,y=340)

#google image resize
image = Image.open(r'logo.png')
logo = image.resize((1,1))

#google logo in login_frame
new_logo = PhotoImage(file=r'logo.png').subsample(20)  # Adjust the subsample factor as needed
# Use the file parameter
logo_login = Label(login_window, image=new_logo,background='white')
logo_login.place(x=20, y=50)

#additional text
Label(login_window,text='Sign in',font='arial 15 ',foreground='black',background='white').place(x=40,y=140)
Label(login_window,text='With your Google account',font='arial 10 ',foreground='black',background='white').place(x=40,y=170)

#user input values

user_input = StringVar()
pass_input = StringVar()
user_entry = Entry(login_window,textvariable=user_input)
user_entry.place(x=200,y=300)
pass_entry = Entry(login_window,textvariable=pass_input)
pass_entry.place(x=200,y=340)

#button sign in 
button_1 = Button(login_window,text='Sign in',font='arial 12',foreground='white',background='#5780d3',relief='flat',command=lambda: check_input(user_input.get(),pass_input.get()))
button_1.place(x=300,y=400)
#check button 
#button_2 forgot password
button_2 = Button(login_window,text='Already have an account..? Log in',font='arial 10 underline',foreground='#5780d3',background='white',relief='flat',command=login_page)
button_2.place(x=40,y=400)
root.mainloop()