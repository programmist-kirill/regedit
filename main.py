import os
import sys

import init
import module
import module_action_windows
import module_action_linux

def main():
    if os.path.exists('action'):
        with open('action') as file:
            action = file.read().strip()
            
            if action == 'write':
                with open('name_element') as name_file:
                    name_element = name_file.read().strip()
                
                with open('value_element') as value_file:
                    value_element = value_file.read().strip()
                    
                with open('type_element') as type_file:
                    type_element = type_file.read().strip()
                
                if os.path.exists('disk_for_program'):
                    with open('disk_for_program') as file:
                        disk_for_program = file.read().strip()

                with open('system') as file:
                    system = file.read().strip()
                
                if os.path.exists('username'):
                    with open('username') as file:
                        username = file.read().strip()
                
                if system == 'Windows':
                    if type_element == 'root':
                        module.write.Windows_root(module_action_windows,disk_for_program,name_element,value_element)

                    if type_element == 'user':
                        module.write.Windows_user(module_action_windows,disk_for_program,name_element,value_element)
                
                if system == 'Linux':
                    if type_element == 'root':
                        module.write.Linux_root(module_action_linux,username,name_element,value_element)

                    if type_element == 'user':
                        module.write.Linux_user(module_action_linux,username,name_element,value_element)
            
            if action == 'delete':
                with open('name_element') as name_file:
                    name_element = name_file.read().strip()
                
                with open('value_element') as value_file:
                    value_element = value_file.read().strip()
                    
                with open('type_element') as type_file:
                    type_element = type_file.read().strip()
                
                if os.path.exists('disk_for_program'):
                    with open('disk_for_program') as file:
                        disk_for_program = file.read().strip()

                with open('system') as file:
                    system = file.read().strip()
                
                if os.path.exists('username'):
                    with open('username') as file:
                        username = file.read().strip()


                if system == 'Windows':
                    if type_element == 'root':
                        module.delete.Windows_root(module_action_windows,disk_for_program,name_element,value_element)

                    if type_element == 'user':
                        module.delete.Windows_user(module_action_windows,disk_for_program,name_element,value_element)
                
                if system == 'Linux':
                    if type_element == 'root':
                        module.delete.Linux_root(module_action_linux,username,name_element,value_element)

                    if type_element == 'user':
                        module.delete.Linux_user(module_action_linux,username,name_element,value_element)
            
            if action == 'check':
                with open('name_element') as name_file:
                    name_element = name_file.read().strip()
                
                with open('value_element') as value_file:
                    value_element = value_file.read().strip()
                    
                with open('type_element') as type_file:
                    type_element = type_file.read().strip()
                
                if os.path.exists('disk_for_program'):
                    with open('disk_for_program') as file:
                        disk_for_program = file.read().strip()

                with open('system') as file:
                    system = file.read().strip()
                
                if os.path.exists('username'):
                    with open('username') as file:
                        username = file.read().strip()


                if system == 'Windows':
                    if type_element == 'root':
                        module.check.Windows_root(module_action_windows,disk_for_program,name_element,value_element)

                    if type_element == 'user':
                        module.check.Windows_user(module_action_windows,disk_for_program,name_element,value_element)
                
                if system == 'Linux':
                    if type_element == 'root':
                        module.check.Linux_root(module_action_linux,username,name_element,value_element)

                    if type_element == 'user':
                        module.check.Linux_user(module_action_linux,username,name_element,value_element)
            
            if action == 'read':

                with open('name_element') as name_file:
                    name_element = name_file.read().strip()
                
                with open('value_element') as value_file:
                    value_element = value_file.read().strip()
                    
                with open('type_element') as type_file:
                    type_element = type_file.read().strip()
                
                if os.path.exists('disk_for_program'):
                    with open('disk_for_program') as file:
                        disk_for_program = file.read().strip()

                with open('system') as file:
                    system = file.read().strip()
                
                if os.path.exists('username'):
                    with open('username') as file:
                        username = file.read().strip()
                

                if system == 'Windows':
                    if type_element == 'root':
                        module.read.Windows_root(module_action_windows,disk_for_program,name_element,value_element)

                    if type_element == 'user':
                        module.read.Windows_user(module_action_windows,disk_for_program,name_element,value_element)
                
                if system == 'Linux':
                    if type_element == 'root':
                        module.read.Linux_root(module_action_linux,username,name_element,value_element)

                    if type_element == 'user':
                        module.read.Linux_user(module_action_linux,username,name_element,value_element)

    else:
        print('File not found')

# инициализация реестра
init.init_regedit()
#инициализация программы
init.init_program()
#инициализация 7zip
init.seven_zip()

# запуск основного цикла
if __name__ == '__main__':
    main()