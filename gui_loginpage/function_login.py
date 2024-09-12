import json
import tkinter.messagebox


def check_record(username,password):
    '''check username and password if exist pass on to next window or raise error msg password is incorrect  '''
    try:
        file  = open('record.json',"r")
        record = file.read()
        final  = json.loads(record)
        if username in final:
            if final[f'{username}'] == password :
                tkinter.messagebox.showinfo("development","Portal is currently under development")
            else:
                from login_main import forgot_diplay_input #type:ignore
        elif not username.strip():
            tkinter.messagebox.showerror('Username',"username could not be empty")
        else:
            tkinter.messagebox.showerror('Username','username does not exist')
        file.close()
    except:
        tkinter.messagebox.showerror('file error','File data lost or file corrupt\nIf u are new pls sign in')