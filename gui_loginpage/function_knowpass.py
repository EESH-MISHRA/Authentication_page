import json
from tkinter import messagebox
'''display forgot password'''
def password(username: str):
    file = open('record.json','r')
    record = file.read()
    final = json.loads(record)
    if username in final:
        return final[f'{username}']
    else:
        messagebox.showerror('username','does not exist')
print(password('eesh'))