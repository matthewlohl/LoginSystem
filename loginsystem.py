granted = False
def grant():
    global granted
    granted = True

def login(username,password):
    success = False
    file = open("users.txt", "r")
    for i in file.readlines():
        a,b = i.split(",")
        b = b.strip()
        if(a==username and b==password):
            success = True
            break
    file.close()
    if (success):
        print("Login success!")
        grant()
    else:
        print("Wrong credentials")
        
def register(username,password): 
    print ("You have been registered")
    file = open("users.txt", "a")
    file.write("\n"+username+","+password)
    file.close()
    grant()

def access(option):
    global username
    global password
    if (option=="login"):
        username = input ("Enter your username: ")
        password = input ("Enter your password: ")
        login (username, password)
    else:
        print ("Enter your username and password to register")
        username = input ("Enter your username: ")
        password = input ("Enter your password: ")
        register (username,password)

def begin():
    global option 
    print ("Welcome to this login page")
    option = input ("Login or Register (login,reg): ")
    if (option !="login" and option != "reg"):
        begin()
begin()
access (option)
if(granted):
    print('Welcome to your account')
    print('*** Please remember your user details: ***')
    print('Username:'+ username +"\n"+'Password: '+password)