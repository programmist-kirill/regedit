import os

import module_action_linux
import module_action_windows

class write:
    def Windows_root(module_action_windows,disk_for_program,name_element,value_element):
        directory_key_root = disk_for_program + '/regedit/key/root.reg'
        directory_new_file = disk_for_program + '/regedit/cashe/root/' + name_element + '.key'

        with open(directory_new_file,'w') as fp:
            fp.write(value_element)

        if os.path.exists(directory_key_root):
            module_action_windows.unzipping.root()

        module_action_windows.zipping.root()


    def Windows_user(module_action_windows,disk_for_program,name_element,value_element):
        directory_key_user = disk_for_program + '/regedit/key/user.reg'
        directory_new_file = disk_for_program + '/regedit/cashe/user/' + name_element + '.key'

        with open(directory_new_file,'w') as fp:
            fp.write(value_element)
        
        if os.path.exists(directory_key_user):
            module_action_windows.unzipping.user()

        module_action_windows.zipping.user()
    
    def Linux_root(module_action_linux,username,name_element,value_element):
        directory_new_file = '/home/' + username + '/regedit/cashe/root/' + name_element + '.key'

        with open(directory_new_file,'w') as fp:
            fp.write(value_element)

        
        directory_for_check_reg = '/home/' + username + '/regedit/key/root.reg'
        if os.path.exists(directory_for_check_reg):
            module_action_linux.unzipping.root()
        

        module_action_linux.archiving.root()
    def Linux_user(module_action_linux,username,name_element,value_element):
        
        directory_new_file = '/home/' + username + '/regedit/cashe/user/' + name_element + '.key'

        with open(directory_new_file,'w') as fp:
            fp.write(value_element)
        
        directory_for_check_reg = '/home/' + username + '/regedit/key/user.reg'
        if os.path.exists(directory_for_check_reg):
            module_action_linux.unzipping.user()

        module_action_linux.archiving.user()

class delete:

    def Windows_root(module_action_windows,disk_for_program,name_element,value_element):

        module_action_windows.unzipping.root()

        os.remove(disk_for_program + '/regedit/cashe/root/' + name_element + '.key')
        
        module_action_windows.archiving.root()
    
    def Windows_user(module_action_windows,disk_for_program,name_element,value_element):
    
        module_action_windows.unzipping.user()

        os.remove(disk_for_program + '/regedit/cashe/user/' + name_element + '.key')

        module_action_windows.archiving.user()   
    def Linux_root(module_action_linux,username,name_element,value_element):
    
        module_action_linux.unzipping.root()

        os.remove('/home/' + username + '/regedit/cashe/root/' + name_element + '.key')

        module_action_linux.Linux_root()
    def Linux_user(module_action_linux,username,name_element,value_element):

        module_action_linux.unzipping.user()

        os.remove('/home/' + username + '/regedit/cashe/user/' + name_element + '.key')

        module_action_linux.archiving.user()
class check:

    def Windows_root(module_action_windows,disk_for_program,name_element,value_element):

        module_action_windows.unzipping.root()

        directory_for_checking = disk_for_program + '/regedit/cashe/root/' + name_element + '.key'
        if os.path.exists(directory_for_checking):
            with open('result_check','w') as fp:
                fp.write('True')
        else:
            with open('result_check','w') as fp:
                fp.write('False')


    def Windows_user(module_action_windows,disk_for_program,name_element,value_element):

        module_action_windows.unzipping.user()

        directory_for_checking = disk_for_program + '/regedit/cashe/user/' + name_element + '.key'
        if os.path.exists(directory_for_checking):
            with open('result_check','w') as fp:
                fp.write('True')
        else:
            with open('result_check','w') as fp:
                fp.write('False')


    def Linux_root(module_action_linux,username,name_element,value_element):

        module_action_linux.unzipping.root()

        directory_for_checking = '/home/' + username + '/regedit/cashe/root/' + name_element + '.key'
        if os.path.exists(directory_for_checking):
            with open('result_check','w') as fp:
                fp.write('True')
        else:
            with open('result_check','w') as fp:
                fp.write('False')
    

    def Linux_user(module_action_linux,username,name_element,value_element):

        module_action_linux.unzipping.user()

        directory_for_checking = '/home/' + username + '/regedit/cashe/user/' + name_element + '.key'
        if os.path.exists(directory_for_checking):
            with open('result_check','w') as fp:
                fp.write('True')
        else:
            with open('result_check','w') as fp:
                fp.write('False')


class read:

    def Windows_root(module_action_windows,disk_for_program,name_element,value_element):

        module_action_windows.unzipping.root()

        directory_for_checking = disk_for_program + '/regedit/cashe/root/' + name_element + '.key'
        with open(directory_for_checking) as file:
            value_element = file.read().strip()

        with open('value_element','w') as fp:
            fp.write(value_element)
    
    def Windows_user(module_action_windows,disk_for_program,name_element,value_element):

        module_action_windows.unzipping.user()

        directory_for_checking = disk_for_program + '/regedit/cashe/user/' + name_element + '.key'
        with open(directory_for_checking) as file:
            value_element = file.read().strip()

        with open('value_element','w') as fp:
            fp.write(value_element)


    def Linux_root(module_action_linux,username,name_element,value_element):

        module_action_linux.unzipping.root()

        directory_for_checking = '/home/' + username + '/regedit/cashe/root/' + name_element + '.key'
        with open(directory_for_checking) as file:
            value_element = file.read().strip()

        with open('value_element','w') as fp:
            fp.write(value_element)
    
    def Linux_user(module_action_linux,username,name_element,value_element):

        module_action_linux.unzipping.user()

        directory_for_checking = '/home/' + username + '/regedit/cashe/user/' + name_element + '.key'
        with open(directory_for_checking) as file:
            value_element = file.read().strip()

        with open('value_element','w') as fp:
            fp.write(value_element)