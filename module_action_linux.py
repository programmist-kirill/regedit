import os

class archiving:
    def root():
        with open('username') as file:
            username = file.read().strip()
            
            directory = '/home/' + username + '/regedit/cashe/root/*.key'
            commande = "7z a -tzip -ssw -mx1 -r0 " + '/home/' + username + '/regedit/key/root.rar ' + directory
            with open('7_Zip_arcvining.sh','w') as fp:
                fp.write(commande)
            os.system('sh 7_Zip_arcvining.sh')

            directory_null = '/home/' + username + '/regedit/key/root.rar'
            directory_one = '/home/' + username + '/regedit/key/root.reg'
            os.rename(directory_null, directory_one)

            with open('action_clear-cashe','w') as fp:
                fp.write('')
            os.system('python clear.py')

    def user():
        with open('username') as file:
            username = file.read().strip()
            
            directory = '/home/' + username + '/regedit/cashe/user/*.key'
            commande = "7z a -tzip -ssw -mx1 -r0 " + '/home/' + username + '/regedit/key/user.rar ' + directory
            with open('7_Zip_arcvining.sh','w') as fp:
                fp.write(commande)
            
            os.system('sh 7_Zip_arcvining.sh')

            directory_null = '/home/' + username + '/regedit/key/user.rar'
            directory_one = '/home/' + username + '/regedit/key/user.reg'
            os.rename(directory_null, directory_one)

            with open('action_clear-cashe','w') as fp:
                fp.write('')
            os.system('python clear.py')

class unzipping:
    def root():
        with open('username') as file:
            username = file.read().strip()

            directory_null = '/home/' + username + '/regedit/key/root.reg'
            directory_one = '/home/' + username + '/regedit/key/root.rar'
            os.rename(directory_null,directory_one)

            directory = '/home/' + username + '/regedit/key/root.rar'
            commande  = "7z x " + directory + ' -o' + '"/home/' + username + '/regedit/cashe/root/"'
            with open('7_Zip_unzipping.sh','w') as fp:
                fp.write(commande)
            os.system('sh 7_Zip_unzipping.sh')

            with open('action_clear-cashe','w') as fp:
                fp.write('')
            os.system('python clear.py')
        
    def user():
        with open('username') as file:
            username = file.read().strip()
            
            directory_null = '/home/' + username + '/regedit/key/user.reg'
            directory_one = '/home/' + username + '/regedit/key/user.rar'
            os.rename(directory_null,directory_one)

            directory = '/home/' + username + '/regedit/key/user.reg'
            commande = "7z x" + directory + ' -o ' + '/home/' + username + '/regedit/cashe/user/'
            with open('7_Zip_unzipping.sh','w') as fp:
                fp.write(commande)
            os.system('sh 7_Zip_unzipping.sh')

            with open('action_clear-cashe','w') as fp:
                fp.write('')
            os.system('python clear.py')

            #7z x c:\temp\archive.7z -o"c:\temp\"
            #7z a -tzip -mx5 -r0 c:\temp\archive.zip c:\temp
