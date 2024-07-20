import os
import shutil

class clear_cashe:
    def Windows():
        print('start module clear cashe is parameter -windows')

        with open('disk_for_program') as file:
            disk_for_program = file.read().strip()

        directory_key_root = disk_for_program + '/regedit/key/root.reg'
        directory_cashe_root = disk_for_program + '/regedit/cashe/root'

        if os.path.exists(directory_key_root):
            shutil.rmtree(directory_key_root)
            os.makedirs(directory_cashe_root, exist_ok=True)

        directory_key_user = disk_for_program + '/regedit/key/user.reg'
        directory_cashe_user = disk_for_program + '/regedit/cashe/user'
        
        if os.path.exists(directory_key_user):
            shutil.rmtree(directory_cashe_user)
            os.makedirs(directory_cashe_user, exist_ok=True)
        
        def clear_parent_folder(disk_for_program):

            directory_action = disk_for_program + '/regedit/action'
            directory_result_check = disk_for_program + '/regedit/result_check'
            directory_type_element = disk_for_program + '/regedit/type_element'
            directory_value_element = disk_for_program + '/regedit/value_element'
            directory_name_element = disk_for_program + '/regedit/name_element'

            if os.path.exists(directory_action):
                os.remove(directory_action)
            
            if os.path.exists(directory_result_check):
                os.remove(directory_result_check)
            
            if os.path.exists(directory_type_element):
                os.remove(directory_type_element)
            
            if os.path.exists(directory_value_element):
                os.remove(directory_value_element)
            
            if os.path.exists(directory_name_element):
                os.remove(directory_name_element)

        clear_parent_folder(disk_for_program)
            

    def Linux():
        print('start module clear cashe is parameter -linux')

        with open('username') as file:
            username = file.read().strip()
        
        directory_key_root = '/home/' + username + '/regedit/key/root.reg'
        directory_cashe_root = '/home/' + username + '/regedit/cashe/root'

        if os.path.exists(directory_key_root):
            shutil.rmtree(directory_cashe_root)
            os.makedirs(directory_cashe_root, exist_ok=True)

        directory_key_user = '/home/' + username + '/regedit/key/user.reg'
        directory_cashe_user = '/home/' + username + '/regedit/cashe/user'
        
        if os.path.exists(directory_key_user):
            shutil.rmtree(directory_cashe_user)
            os.makedirs(directory_cashe_user, exist_ok=True)
        
        def clear_parent_folder(username):
    
            directory_action = '/home/' + username + '/regedit/action'
            directory_result_check = '/home/' + username + '/regedit/result_check'
            directory_type_element = '/home/' + username + '/regedit/type_element'
            directory_value_element = '/home/' + username + '/regedit/value_element'
            directory_action_clear_cashe = '/home/' + username + '/regedit/action_clear-cashe'
            directory_name_element = '/home/' + username + '/regedit/name_element'

            if os.path.exists(directory_action):
                os.remove(directory_action)
            
            if os.path.exists(directory_result_check):
                os.remove(directory_result_check)
            
            if os.path.exists(directory_type_element):
                os.remove(directory_type_element)
            
            if os.path.exists(directory_value_element):
                os.remove(directory_value_element)
            
            if os.path.exists(directory_action_clear_cashe):
                os.remove(directory_action_clear_cashe)
            
            if os.path.exists(directory_name_element):
                os.remove(directory_name_element)

        clear_parent_folder(username)
    
class init:
    def init_clear():
        print('start module clear init')
        with open('system') as file:
            system = file.read().strip()

        a = True

        while a == True:
            if os.path.exists('action_clear-cashe'):
                a = False
                if system == 'Windows':
                    clear_cashe.Linux()
                    break
                if system == 'Linux':
                    clear_cashe.Linux()
                    break
            else:
                a = True
                continue
    init_clear()