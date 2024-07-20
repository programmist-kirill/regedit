import os

def init_regedit():
    print('init regedit')

def init_program():
    import os
    import getpass

    def get_system_info():
        system = os.uname().sysname if os.name == 'posix' else os.name
        username = getpass.getuser()
        return system, username

    system, username = get_system_info()
    if system == 'Windows':
        with open('system','w') as fp:
            fp.write(system)

        disk_for_program = input('На каком диске находится программа(пример =  C:/),если программа находится не в корне , введите диск и название папки(папка regedit не считается) , окончание / = ')
        if os.path.exists(disk_for_program + 'main.py'):
            print('directory true')
            with open('disk_for_program'):
                fp.write(disk_for_program)
        else:
            a = 0

    if system == 'Linux':
        with open('system','w') as fp:
            fp.write(system)
    
        with open('username','w') as fp:
            fp.write(username)
        
def seven_zip():
    with open('system') as file:
        system = file.read().strip()
    
    if system == 'Windows':
        if os.path.exists('7_zip'):
            print('7_zip true')
        else:
            directory_7z = input('где находится 7zip - ')
            if os.path.exists(directory_7z):
                print('7zip true')
                with open('7_zip','w') as fp:
                    fp.write(directory_7z)
            else:
                a = 0
                while a == 0:
                    directory_7z = input('где находится 7zip - ')
                    if os.path.exists(directory_7z):
                        print('7zip true')
                        with open('7_zip','w') as fp:
                            fp.write(directory_7z)
                        a = 1
                        break
                    else:
                        print('7zip false')
                        a = 0
                        continue