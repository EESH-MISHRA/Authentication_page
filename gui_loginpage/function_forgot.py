import json
from tkinter import messagebox
from forgot_pass  import *
def get_password(username):

    file = open('record.json','r')
    record = file.read()
    final = json.loads(record)
    if username in final:
        pass_output.set(final[username])
    elif not username.strip():
        messagebox.showerror("username","username cannot be empty")
    else:
        messagebox.showerror('username','does not exist')