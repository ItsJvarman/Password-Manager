from cryptography.fernet import Fernet

'''
def write_key():

    key= Fernet.generate_key()
    with open('Projects/key.key','wb') as key_file:
        key_file.write(key)
write_key() 
'''

def load_key():
    file=open('Projects/key.key','rb')
    key=file.read()
    file.close()
    return key


master_pwd=input("Type the Master Password: ")
key=load_key()+ master_pwd.encode()
fer=Fernet(key)




def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('Projects/password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('Projects/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "  Password:", fer.decrypt(passw.encode()).decode())

while True:
    mode=input("Are you want to add  or view passwords or quit (add/view/q) ").lower()
    if mode=='q':
        break
    if mode=='add':
        add()
    elif mode=='view':
        view()
    else:
        print("Invalid Input")
        continue    