'''tkinter program :- login portal '''
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image
import json
#redirect window
def login_window():
    root.destroy()
    import login_main #type: ignore
    if __name__=='__main__':
        login_window
#display forgot password
'''display forgot password'''
def get_password():
    try:
        username = user_input.get()
        file = open('record.json','r')
        record = file.read()
        final = json.loads(record)
        if username in final:
            pass_output.set(final[username])
        elif not username.strip():
            messagebox.showerror("username","username cannot be empty")
        else:
            messagebox.showerror('username','does not exist')
    except:
        messagebox.showerror('file error',"File not exist")


root = Tk()
# Bitmap icon
root.iconbitmap(r'icon.ico')
#title
root.title('FORGOT PASSWORD ')
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
forgot_window = Frame(root,background='white',highlightbackground='black',highlightthickness=1)
forgot_window.place(relx=0.5,rely=0.5,anchor='center',height=650,width=540)  # Centered placement
#username label
username_label = Label(forgot_window,text='Username',font='arial 10 bold',foreground='black',background='white')
username_label.place(x=50,y=300)
#password label
pasword_label = Label(forgot_window,text='Password',font='arial 10 bold',foreground='black',background='white')
pasword_label.place(x=50,y=340)

#google image resize
image = Image.open(r'logo.png')
logo = image.resize((1,1))

#google logo in login_frame
new_logo = PhotoImage(file=r'logo.png').subsample(20)  # Adjust the subsample factor as needed
# Use the file parameter
logo_forgot = Label(forgot_window, image=new_logo,background='white')
logo_forgot.place(x=20, y=50)

#additional text
Label(forgot_window,text='FORGOT PASSWORD',font='arial 15 ',foreground='black',background='white').place(x=40,y=140)
Label(forgot_window,text='of your Google account',font='arial 10 ',foreground='black',background='white').place(x=40,y=170)
#user input values

user_input = StringVar()
pass_output = StringVar()
user_entry = Entry(forgot_window,textvariable=user_input)
user_entry.place(x=200,y=300)
#refresh
def refresh(event):
    pass_output.set('')  # Assuming `pass_output` is a StringVar or similar

# Bind the refresh function to the button click event
user_entry.bind('<Button-1>', refresh)
#button know password
button_1 = Button(forgot_window,text='know your password',font='arial 10',foreground='white',background='#5780d3',relief='flat',command =get_password)
button_1.place(x=300,y=400)
Label(forgot_window,textvariable=pass_output,font='arial 10',foreground='black',background='white').place(x=200,y=340)
#sign redirect page 
Button(forgot_window,text="Log in",foreground="#5780d3",font="arial 10 underline",relief='flat',background='white',command=login_window).place(x=50,y=405)
root.mainloop()