#                                  Folder Checker
#
# for Python 3
# ©Anime no Sekai - 2020
#

# Imports
from time import sleep
from datetime import date
from datetime import datetime

import subprocess
import os
import shutil

# Variable declaration
folder_path = ''
folder_name = ''
folder_check_result_folder = ''
destination_folder = ''
deletedfiles = []
moved_to_trash_files = []
kept_files = []

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
    sleep(0.1)
    folder_path = input('> ')
    indexes_of_slash = [i for i, ltr in enumerate(folder_path) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = folder_path[index + 1 - number_of_iterations]
        print(character_after_slash)
        if character_after_slash == ' ':
            folder_path = folder_path[:index - number_of_iterations] + folder_path[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    if folder_path.lower() == 'cancel' or folder_path.lower() == 'stop' or folder_path.lower() == 'quit' or folder_path.lower() == 'exit':
        goodbye_message()
    elif not os.path.isdir(folder_path):
        subprocess.call("clear", shell=True, universal_newlines=True)
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
    global folder_name

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
    subprocess.call("clear", shell=True, universal_newlines=True)
    # Commands
    print("Commands available")
    print('____________________________')
    print('')
    print(" 'o' or 'open'       >    to open the file")
    print("'rev' or 'reveal'    >    to reveal the file in your file explorer")
    print(" 'r' or 'remove'     >    to move the file into the trash folder")
    print(" 'R'                 >    to delete the file permanently")
    print(" '-R'                >    to delete the file permanently (without confirmation)")
    print("'stop' or 'cancel'   >    to stop the execution")
    print('')
    print(" - Any other key to keep the file in his location - ")
    print('')
    print('')
    print('')
    input('Press any key to continue...')
    subprocess.call("clear", shell=True, universal_newlines=True)
    list_of_files_in_folder = os.listdir(folder_path)
    kept_files = list_of_files_in_folder
    for file in list_of_files_in_folder:
        if file == __file__:
            continue
        if file == 'Folder Check':
            continue
        if file == '.DS_Store':
            continue
        subprocess.call("clear", shell=True, universal_newlines=True)
        def user_decision():
            print('What do you want to do with the file/folder: ' + file)
            user_input = input('> ')
            if user_input == 'o' or user_input == 'open':
                open_file(file)
                display_action('Opening you file')
                user_decision()
            elif user_input == 'r' or user_input == 'remove':
                move_to_trash_folder(file)
                display_action('Moving your file to the trash folder')
            elif user_input == 'R':
                print('This file will be deleted permanently')
                confirmation = input('Type [yes] if you really want to delete it or anything else to abort: ')
                if confirmation.lower() == 'yes':
                    remove(file)
                    display_action('Deleting your file')    
                else:
                    user_decision()
            elif user_input == '-R' or user_input == 'removenow':
                remove(file)
                display_action('Deleting your file')
            elif user_input.lower() == 'reveal' or user_input.lower() == 'rev':
                reveal(file)
                display_action('Revealing the file in your file explorer')
                user_decision()
            elif user_input.lower() == 'stop' or user_input.lower() == 'cancel' or user_input.lower() == 'exit' or user_input.lower() == 'quit':
                display_action('Stoping')
                goodbye_message()
            elif user_input != '':
                print('No known command detected')
                print('Next File!')
                sleep(2)
            else:
                print('Next File!')
                sleep(1)
        user_decision()
    subprocess.call("clear", shell=True, universal_newlines=True)
    print('Done!')
    sleep(2)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Do you want a summary of all actions?")
    user_choice_on_summary = input("Type [no] for no summary: ")
    if user_choice_on_summary.lower() == 'no':
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('Ok!')
        sleep(2)
        goodbye_message()
    else:
        # Deleted files
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('Here are the permanently deleted files')
        print('___________________________________________')
        print('')
        file_number = 0
        for deletedfile in deletedfiles:
            file_number += 1
            print(deletedfile)
        if file_number == 0:
            print("No deleted file.")
        print('')
        print('Total: ' + str(file_number))
        input('Press any key to continue...')
        # Moved to trash files
        subprocess.call("clear", shell=True, universal_newlines=True)
        print('Here are the files moved to trash')
        print('___________________________________________')
        print('')
        file_number = 0
        for movedfile in moved_to_trash_files:
            file_number += 1
            print(movedfile)
        if file_number == 0:
            print("No file got moved to trash.")
        print('')
        print('Total: ' + str(file_number))

        input('Press any key to continue...')

        # Kept files
        for file in deletedfiles:
            kept_files.remove(file)
        for file in moved_to_trash_files:
            kept_files.remove(file)

        subprocess.call("clear", shell=True, universal_newlines=True)
        print('Here are the kept files')
        print('___________________________________________')
        print('')
        file_number = 0
        for file in kept_files:
            file_number += 1
            print(file)
        if file_number == 0:
            print("No file got kept in the folder.")
        print('')
        print('Total: ' + str(file_number))

        end_choice = input('Press [any key] to quit or [save] to save this summary to a file... ')
        if end_choice.lower() == 'save' or end_choice.lower() == 'ave' or end_choice.lower() == 'sve' or end_choice.lower() == 'sae' or end_choice.lower() == 'sav' or end_choice.lower() == 'export' or end_choice.lower() == 'download':
            display_action('Creating your file')
            os.chdir(destination_folder)
            summary_file = open("summary_file.txt", "w+")

            summary_file.write("Here is the summary of all actions taken on the folder: {} \n".format(folder_name))
            summary_file.write(datetime.now().strftime("%B, the %d of %Y") + '\n')

            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')

            summary_file.write('Here are the permanently deleted files\n')
            summary_file.write('___________________________________________\n')
            summary_file.write('\n')
            file_number = 0
            for deletedfile in deletedfiles:
                file_number += 1
                summary_file.write(deletedfile + '\n')
            if file_number == 0:
                summary_file.write("No deleted file.\n")
            
            number_of_permanently_deleted_files = file_number
            summary_file.write('\n')
            summary_file.write('Total: ' + str(file_number) + '\n')

            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')

            summary_file.write('Here are the files moved to trash\n')
            summary_file.write('___________________________________________\n')
            summary_file.write('\n')
            file_number = 0
            for movedfile in moved_to_trash_files:
                file_number += 1
                summary_file.write(movedfile + '\n')
            if file_number == 0:
                summary_file.write("No file got moved to trash.\n")
            
            number_of_files_moved_to_trash = file_number
            summary_file.write('\n')
            summary_file.write('Total: ' + str(file_number) + '\n')

            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')

            summary_file.write('Here are the kept files\n')
            summary_file.write('___________________________________________\n')
            summary_file.write('\n')
            file_number = 0
            for file in kept_files:
                file_number += 1
                summary_file.write(file + '\n')
            if file_number == 0:
                summary_file.write("No file got kept in the folder.\n")

            number_of_kept_files = file_number
            summary_file.write('\n')
            summary_file.write('Total: ' + str(file_number) + '\n')
            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('TOTAL OF FILES: {}\n'.format(number_of_files_moved_to_trash + number_of_kept_files + number_of_permanently_deleted_files))
            summary_file.write('\n')
            summary_file.write('\n')
            summary_file.write('Generated by Folder Checker\n')
            summary_file.write('©Anime no Sekai - 2020')

            summary_file.close()

        display_action('Opening the result folder')
        subprocess.call(["open", "-R", destination_folder])
        sleep(1)
        goodbye_message()





# Decision responses
def open_file(file):
    file_path = folder_path + '/' +  file
    subprocess.run(['open', file_path], check=True)

def move_to_trash_folder(file):
    global moved_to_trash_files
    file_path = folder_path + '/' +  file
    shutil.move(file_path, destination_folder)
    moved_to_trash_files.append(file)

def remove(file):
    global deletedfiles
    file_path = folder_path + '/' +  file
    shutil.rmtree(file_path)
    deletedfiles.append(file)

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

# Good Bye message
def goodbye_message():
    subprocess.call("clear", shell=True, universal_newlines=True)
    print('Thank you for using this program!')
    sleep(1)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("F")
    sleep(0.2)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Fo")
    sleep(0.18)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Fol")
    sleep(0.15)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Fold")
    sleep(0.11)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folde")
    sleep(0.06)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder")
    sleep(0.07)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder C")
    sleep(0.09)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder Ch")
    sleep(0.13)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder Che")
    sleep(0.16)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder Check")
    sleep(0.18)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder Checke")
    sleep(0.19)
    subprocess.call("clear", shell=True, universal_newlines=True)
    print("Folder Checker")
    sleep(2)
    print('')
    print('© Anime no Sekai - 2020')
    print('')
    sleep(3)
    quit()


initialization()