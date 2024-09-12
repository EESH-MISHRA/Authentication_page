import random
import string 
def encoder(user_id:str,pass_id):
    '''encrypt user data by adding random char and digits in the start and the end of the reversed username  '''
    update_user = user_id[::-1]
    update_pass_id = pass_id[::-1]
    encrypt = string.ascii_letters + string.digits
    rand = "".join(random.choices(encrypt,k=10))
    encoded_user_id = rand+update_user+rand[::-1]
    encoded_pass_id = rand+update_pass_id+rand[::-1]
    global username,password
    username = encoded_user_id
    password = encoded_pass_id
def decoder(encoded_user:str,encoded_pass:str,length_encoded_user:int,length_encoded_pass:int):
    '''decode the data by removing char and digits from the start and end of the username and reversed username  '''
    decoded_user = encoded_user[10:length_encoded_user-10][::-1]
    decoded_pass = encoded_pass[10:length_encoded_pass-10][::-1]
    global