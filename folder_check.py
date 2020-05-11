#                                  Folder Checker
#
# for Python 3
# ©Anime no Sekai - 2020
#

# Imports
from time import sleep
from datetime import date

import subprocess
import os
import shutil

# Variable declaration
folder_path = ''
folder_check_result_folder = ''
destination_folder = ''

# Initialization
def initialization():
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("         - Welcome on Folder Checker! -       ")
    print('')
    print("by Anime no Sekai")
    print('')
    print('')
    ask_for_folder_path()

# Asking for the folder to check
def ask_for_folder_path():
    global folder_path

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
        display_action("Loading the folder")

        create_session_folder()

# Creating the session folder
def create_session_folder():
    global destination_folder
    global folder_check_result_folder
    global folder_path

    if folder_path.endswith('/'):
        folder_path = folder_path[:-(1)]
    folder_check_result_folder = "{}/Folder Check".format(folder_path)
    
    if not os.path.isdir(folder_check_result_folder):
        os.makedirs(folder_check_result_folder)
        create_session_folder()

    index_of_last_slash = folder_path.rfind('/')
    folder_name = folder_path[index_of_last_slash:]

    results_folder = folder_check_result_folder + '/' + folder_name + ' ' + str(date.today())

    number = 0
    if os.path.isdir(results_folder):
        number += 1
    while os.path.isdir(results_folder + ' ' + str(number)):
        number += 1
    number = str(number)
    if number == '0':
        os.makedirs(results_folder)
        destination_folder = results_folder
    else:
        os.makedirs(results_folder + ' ' + number)
        destination_folder = results_folder + ' ' + number
    
    core()

# The core of the program, asking the user to take a decision on all files of the folder
def core():
    list_of_files_in_folder = os.listdir(folder_path)
    for file in list_of_files_in_folder:
        if file == __file__:
            continue
        if file == 'Folder Check':
            continue
        if file == '.DS_Store':
            continue
        subprocess.call("clear", shell=True, universal_newlines=True)
        def user_decision():
            print('What do you want to do with the file: ' + file)
            user_input = input('> ')
            if user_input == 'o' or user_input == 'open':
                open_file(file)
                display_action('Opening you file')
                user_decision()
            elif user_input == 'r' or user_input == 'remove':
                move_to_trash_folder(file)
                display_action('Moving your file to the trash folder')
            elif user_input == '-R' or user_input == 'removenow':
                remove(file)
                display_action('Deleting your file')
            elif user_input == 'reveal' or user_input == 'rev':
                reveal(file)
                display_action('Revealing the file in your file explorer')
                user_decision()
            elif user_input != '':
                print('No known command detected')
                sleep(2)
            print('Next File!')
            sleep(1)
        user_decision()
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('Done!')
        print()

# Decision responses
def open_file(file):
    file_path = folder_path + '/' +  file
    subprocess.run(['open', file_path], check=True)

def move_to_trash_folder(file):
    file_path = folder_path + '/' +  file
    shutil.move(file_path, destination_folder)

def remove(file):
    file_path = folder_path + '/' +  file
    shutil.rmtree(file_path)

def reveal(file):
    file_path = folder_path + '/' +  file
    subprocess.call(["open", "-R", file_path])


# Nice way to display performed actions to the user
def display_action(action_to_display):
    for _ in range(2):
        subprocess.call("clear", shell=True, universal_newlines=True)
        print(action_to_display + ".")
        sleep(0.15)
        subprocess.call("clear", shell=True, universal_newlines=True)
        print(action_to_display + "..")
        sleep(0.15)
        subprocess.call("clear", shell=True, universal_newlines=True)
        print(action_to_display + "...")
        sleep(0.15)

initialization()