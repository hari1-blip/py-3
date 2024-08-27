from cryptography.fernet import Fernet


main_pass = input('enter the master password:')
def write_key ():
    key = Fernet.generate_key()
    with open ('key.key','wb')as file:
        file.write(key)

write_key()
def add():
    name = input('enter the user name:')
    passw = input('enter the password: ')
    with open('password.txt','a') as f:
        f.write('name:' + name +'\n'+ 'passw:' + passw + '\n' + '----------------------------'+'\n')


def view():
    with open('password.txt','r')as f:
        for lines in f:
            print (lines)

while True:
    mode = input('what would you like to do (add,view) , press q to quit\n enter the choice:')

    if (mode == 'add'):
        add()

    elif (mode == 'view'):
        view()

    elif(mode == 'q'):
        break

    else:
        print('enter a valid option:')



    