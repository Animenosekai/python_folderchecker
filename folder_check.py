#                                  Folder Checker
#
# for Python 3
# ©Anime no Sekai - 2020
#

# Imports
from time import sleep
import subprocess
import os
from datetime import datetime
import shutil

folder_path = ''
folder_check_result_folder = ''

def initialization():
    global folder_path
    print(" - Welcome on Folder Checker! - ")
    print('')
    print("by Anime no Sekai")
    print('')
    print('')

def ask_for_folder_path():
    global folder_check_result_folder
    print("What is the path to the folder you wanna check today?")
    folder_path = input('> ')
    if not os.path.isdir(folder_path):
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('')
        print('You mistyped something in your folder path')
        sleep(1)
        print('Please try again...')
        sleep(2)
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('')
        ask_for_folder_path()
    else:
        for _ in range(2):
            subprocess.call("clear", shell=True, universal_newlines=True)
            print("Loading the folder.")
            sleep(0.15)
            subprocess.call("clear", shell=True, universal_newlines=True)
            print("Loading the folder..")
            sleep(0.15)
            subprocess.call("clear", shell=True, universal_newlines=True)
            print("Loading the folder...")
            sleep(0.15)
        folder_check_result_folder = folder_path + '/Folder Check'
        if folder_path.endswith('/'):
            folder_path = folder_path[:-(1)] 
        if os.path.isdir(folder_check_result_folder):
            create_session_folder()
        else:
            os.makedirs(folder_check_result_folder)
            create_session_folder()

def create_session_folder():
    index_of_last_slash = folder_path.rfind('/')
    folder_name = folder_path[index_of_last_slash:]
    now = datetime.now()
    os.makedirs(folder_check_result_folder + '/' + folder_name + ' ' + now.strftime("%d/%m/%Y %H:%M:%S"))
    destination_folder = folder_check_result_folder + '/' + folder_name + ' ' + now.strftime("%d/%m/%Y %H:%M:%S")

def core():
    list_of_files_in_folder = os.listdir(folder_path + '/')
    for file in list_of_files_in_folder:
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('What do you want to do with the file: ' + file)
        def user_decision():
            user_input = input('> ')
            if user_input is 'o' or user_input is 'open':
                open(file)
                print('Opening your file...')
                sleep(2)
                user_decision()
            elif user_input is 'r' or user_input is 'remove':
                move_to_trash_folder(file)
                print('Moving your file to the trash folder...')
                sleep(2)
                user_decision()
            elif user_input is '-R' or user_input is 'removenow':
                remove(file)
                print('Deleting your file...')
                sleep(2)
                user_decision()
            elif user_input is 'reveal' or user_input is 'rev':
                reveal(file)
                print('Revealing in your file explorer...')
                sleep(2)
                user_decision()
            print('Next File!')
            sleep(1)

def open(file_path):
    os.startfile(file_path)

def move_to_trash_folder(file_path):
    shutil.move(file_path, destination_folder)

def remove(file_path):
    os.remove(file_path)

def reveal(file_path):
    subprocess.call(["open", "-R", file_path])

initialization()