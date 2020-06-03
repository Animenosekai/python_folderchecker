# python_folderchecker
 A python script which lets you review each file of a folder and decide wether you want to keep the file, put it in a "trash" folder or delete it permanently.
 
 ### Installation
 
 #### WITH PIP
 - Open your command-prompt/terminal
 - Run `pip install foldercheck`
 
 #### MANUALLY
 - Download or clone this repository
 - Unzip if needed
 - You can now directly open `folder_check.py` and start reviewing your folders!
 
> (On macOS you have a special script to open it `Open Folder Check on macOS` because you can't just double click it (it could prompt you to a script editor) )
 
 ### Dependencies
 - Python 3 (downloadable at https://www.python.org/downloads/)
 
 ### Platform/Working OS
 - This python script is cross-platform and has been tested on macOS and Windows.
 
 > However, some functionnalities might not be available on every operating system (i.e. `reveal` on Windows which will just open the folder you're checking)
 
 ### Usage
 Folder Checker (for Python) usage is very simple.
 
#### WHILE INSTALLED WITH PIP
- Open your command-prompt/terminal in the folder you want to check (or `cd` into it)
- type `foldercheck`

#### WHILE INSTALLED MANUALLY
 - Open the file (with Python) and you will be prompted to enter the path of the folder you want to review (tips: you can also simply drag and drop the folder into the terminal).
 - Press `enter` to continue after looking at the available commands.
 - Decide what you want to do for each file and folder of the folder!
 
 
 ### Commands when deciding what to do with a file/folder
- `o` or `open`       >    to open the file
- `rev` or `reveal`    >    to reveal the file in your file explorer
- `r` or `remove`     >    to move the file into the trash folder
- `R`                 >    to delete the file permanently
- `-R`                >    to delete the file permanently (without confirmation)
- `stop` or `cancel`   >    to stop the execution


### Troubleshooting
If you have a problem or a bug, please report it under the `Issues` section of this repo.

You might be asked to install psutil via pip (`pip install psutil`) which will give multiple system and hardware information.

You might also be asked to open the file with a terminal/command prompt with the debug argument (`python3 folder_check.py -d > troubleshoot.txt`)

### File filtering
You won't be able to move or delete github (`.git` and `.gitattributes`) files, `.DS_Store` files, the `Folder Check` folder and the `folder_check` python script itself because they are not intended to move or are hidden for a good reason (i.e. `.DS_Store` files stores informations about the location of files in a folder for the `Finder` on macOS)

Also, you will be asked for a confirmation on system files before deleting or moving them. (do not rely on this though, this is in case of an accident and isn't perfect, always verify what the file is before doing anything on it (and you sure shouldn't delete any system files))

I am not responsible for any damage that might be caused by my script, or any bad usage of this script.



© Anime no Sekai - 2020
