import os


class archiving:
    def root():
        with open('7_zip') as file:
            directory_7z = file.read().strip()

        with open('disk_for_program') as file:
            disk_for_program = file.read().strip()

        directory = disk_for_program + '/regedit/cashe/root/*.key'
        commande = "cd " + directory_7z + "\n" + "7z a -tzip -ssw -mx1 -r0 " + disk_for_program + "/regedit/key/root.rar" + directory
        with open('7_Zip_arcvining.bat') as fp:
            fp.write(commande)
        
        os.system(r'7_Zip_arcvining.bat')

        directory_null = disk_for_program + 'regedit/key/root.rar'
        directory_one = disk_for_program + 'regedit/key/root.reg'
        os.rename(directory_null, directory_one)

        with open('action_clear-cashe','w') as fp:
            fp.write('')
        os.system('python clear.py')
    def user():
        with open('7_zip') as file:
            directory_7z = file.read().strip()

        with open('disk_for_program') as file:
            disk_for_program = file.read().strip()

        directory = disk_for_program + '/regedit/cashe/user/*.key'
        commande = "cd " + directory_7z + "\n" + "7z a -tzip -ssw -mx1 -r0 " + disk_for_program + "/regedit/key/user.rar" + directory
        with open('7_Zip_arcvining.bat') as fp:
            fp.write(commande)
        
        os.system(r'7_Zip_arcvining.bat')

        directory_null = disk_for_program + 'regedit/key/user.rar'
        directory_one = disk_for_program + 'regedit/key/user.reg'
        os.rename(directory_null, directory_one)

        with open('action_clear-cashe','w') as fp:
            fp.write('')
        os.system('python clear.py')
class unzipping:
    def root():
        with open('7_zip') as file:
            directory_7z = file.read().strip()

        with open('disk_for_program') as file:
            disk_for_program = file.read().strip()

        directory = disk_for_program + '/regedit/key/root.reg'
        commande = "cd " + directory_7z + "\n" + "7z x" + directory + ' -0' + disk_for_program + "/regedit/cashe/root"
        with open('7_Zip_unzipping.bat') as fp:
            fp.write(commande)
        
        os.system(r'7_Zip_unzipping.bat')

        with open('action_clear-cashe','w') as fp:
            fp.write('')
        os.system('python clear.py')
    def user():
        with open('7_zip') as file:
            directory_7z = file.read().strip()

        with open('disk_for_program') as file:
            disk_for_program = file.read().strip()

        directory = disk_for_program + '/regedit/key/user.reg'
        commande = "cd " + directory_7z + "\n" + "7z x -o" + disk_for_program + "regedit/cashe/user"
        with open('7_Zip_unzipping.bat') as fp:
            fp.write(commande)

        os.system(r'7_Zip_unzipping.bat')

        with open('action_clear-cashe','w') as fp:
            fp.write('')
        os.system('python clear.py')
