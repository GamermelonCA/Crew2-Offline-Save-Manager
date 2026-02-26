import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path
import ctypes.wintypes
import xml.etree.ElementTree as ET

def CheckForCrewFolder():

    global crew2_folder

    CSIDL_PERSONAL = 5
    SHGFP_TYPE_CURRENT = 0

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(
        None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf
    )

    documents_path = Path(buf.value)

    crew2_folder = documents_path / "The Crew 2"

    return crew2_folder.exists() and crew2_folder.is_dir()


def CheckFirstLaunch():
    #this will check the config file to see if it has been launched before

    #true is first launch false is not

    tree = ET.parse("Config.xml")
    ConfigData = tree.getroot()

    first_launch = ConfigData.find("FirstLaunch").text == "1"
    print(first_launch)
    
    return first_launch

def SaveSetup():

    global Status
    global FirstLaunch
    global crew2_folder
    global root

    SaveManage_folder = crew2_folder / "SaveManager Saves"

    if not SaveManage_folder.exists() and not SaveManage_folder.is_dir():
        if not FirstLaunch:
            messagebox.showerror("Missing Folder", """The "SaveManager Saves" Folder could not be found
A new one has been created
If this folder is deleted then all inactive saves are lost""")
        if FirstLaunch:
            messagebox.showinfo("SaveManager Folder", """A "SaveManager Saves" Folder has been created
If this folder is deleted then all inactive saves are lost""")

        SaveManage_folder.mkdir()

    #This function is in charge of loading the saves into gui
    #And file management

    DefaultUI()


    tree = ET.parse("Config.xml")
    ConfigData = tree.getroot()

    first_launch = ConfigData.find("FirstLaunch").text == "1"


    root.mainloop()

def DefaultUI():

    global root
    
    root = tk.Tk()
    root.title("Crew 2 Save Manager")
    root.geometry("900x700")
    root.lift()

    menubar = tk.Menu(root)
    root.configure(menu = menubar)

    sub_menu0 = tk.Menu(root, activeborderwidth=1, borderwidth=1, tearoff=0)
    menubar.add_cascade(compound='left', label='Config', menu=sub_menu0)
    sub_menu0.add_command(compound='left', label='Set Crew 2 Folder')
    sub_menu0.add_command(compound='left', label='Set Crew 2 EXE')
    sub_menu0.add_separator()
    sub_menu0.add_command(compound='left', label='Validate & Refresh')
    sub_menu0.add_separator()
    sub_menu0.add_command(compound='left', label='First Setup Configuration')
    
    sub_menu1 = tk.Menu(root, activeborderwidth=1, borderwidth=1, tearoff=0)
    menubar.add_cascade(compound='left', label='File', menu=sub_menu1)
    sub_menu1.add_command(compound='left', label='Export Active Save')
    sub_menu1.add_command(compound='left', label='Import Save')
    
    sub_menu2 = tk.Menu(menubar, activeborderwidth=1, borderwidth=1, tearoff=0)
    menubar.add_cascade(compound='left', font="TkDefaultFont", label='Help', menu=sub_menu2)
    sub_menu2.add_command(compound='left', label='Setup Instructions')
    sub_menu2.add_command(compound='left', label='Exporting Online save Offline')


    LeftFrame = tk.Frame(root, bg='red')
    LeftFrame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

    MiddleFrame = tk.Frame(root)
    MiddleFrame.pack(side=tk.LEFT, pady=5, expand=False, fill=tk.Y)

    RightFrame = tk.Frame(root, bg='blue')
    RightFrame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

    Separator = ttk.Separator(MiddleFrame, orient=tk.VERTICAL)
    Separator.pack(side=tk.LEFT, padx=5, pady=5, expand=False, fill=tk.Y)

    ActiveSaveBox = tk.Frame(LeftFrame, bg='orange')
    ActiveSaveBox.pack(side=tk.TOP, padx=5, pady=5, ipady=20, expand=False, fill=tk.NONE)

    ActiveSaveText = tk.Label(ActiveSaveBox, bg='yellow', text="Current Save: Not Configured")
    ActiveSaveText.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

    Separator2 = ttk.Separator(LeftFrame, orient=tk.HORIZONTAL)
    Separator2.pack(side=tk.TOP, padx=5, pady=5, expand=False, fill=tk.X)

    NewSaveButton = tk.Button(LeftFrame, text="+ New Save")
    

    SavesBox = ttk.Treeview(LeftFrame)
    SavesBox.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)


    ActivateButton = tk.Button(RightFrame, text="Activate")
    ActivateButton.pack(side=tk.BOTTOM, padx=5, pady=5, ipady=10, expand=False, fill=tk.X)

    SelectedSaveName = tk.Label(RightFrame, text="No Save Selected")
    SelectedSaveName.pack(side=tk.TOP, padx=5, pady=5, ipady=5, expand=False, fill=tk.X)

    
    

if __name__ == '__main__':

    global Status
    global FirstLaunch
    
    #first launch
    #dose checks and launches ui

    Status = CheckForCrewFolder()
    
    if not Status:
        messagebox.showwarning("Loading Error", """Crew 2 Folder Not Found:
Please input location in configuration""")

    FirstLaunch = CheckFirstLaunch()

    if FirstLaunch:
        messagebox.showinfo("First Launch","""For the program to work correctly
Please go to: Config > First Setup Configuration""")

    SaveSetup()
    

    
    
