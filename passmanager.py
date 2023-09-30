from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read
    file.close
    return key


mpwd = input("Master Password: ")
key = load_key() + mpwd.bytes
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Pass: ", str(fer.decrypt(passw.encode())))
                  
    

def add():
    name = input("Username: ")
    pwd = input("Password: ")
    accplat = input("Platform of the account: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) +" (" + accplat +")"+ "\n")
        print("\nAccount stored successfuly!")


while True:
    md = input("\nAdd a Password [1], View Existing Passwords [2] or Quit [3]: ").lower()
    if md == "3":
        print("Have a great day!")
        break
    
    if md == "1":
        add()
    elif md == "2":
        view()
    else:
        print("Not a valid option, try again.")
        continue