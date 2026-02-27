import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import C2SaveManager_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        
        top.title("Crew 2 Save Manager")
        top.geometry("900x700")

        self.top = top
        root = self.top

        self.menubar = tk.Menu()
        top.configure(menu = self.menubar)

        self.sub_menu0 = tk.Menu(root, activeborderwidth=1, borderwidth=1, tearoff=0)
        self.menubar.add_cascade(compound='left', label='Config', menu=self.sub_menu0)
        self.sub_menu0.add_command(compound='left', label='Set Crew 2 Folder')
        self.sub_menu0.add_command(compound='left', label='Set Crew 2 EXE')
        self.sub_menu0.add_separator()
        self.sub_menu0.add_command(compound='left', label='Validate & Refresh')
        #self.sub_menu0.add_separator()
        #self.sub_menu0.add_command(compound='left', label='First Setup Configuration', command=C2SaveManager_support.FirstSetup)
        
        self.sub_menu1 = tk.Menu(root, activeborderwidth=1, borderwidth=1, tearoff=0)
        self.menubar.add_cascade(compound='left', label='File', menu=self.sub_menu1)
        self.sub_menu1.add_command(compound='left', label='Export Active Save')
        self.sub_menu1.add_command(compound='left', label='Import Save')
        
        self.sub_menu2 = tk.Menu(self.menubar, activeborderwidth=1, borderwidth=1, tearoff=0)
        self.menubar.add_cascade(compound='left', font="TkDefaultFont", label='Help', menu=self.sub_menu2)
        self.sub_menu2.add_command(compound='left', label='Setup Instructions')
        self.sub_menu2.add_command(compound='left', label='Exporting Online save Offline')


        self.LeftFrame = tk.Frame(root, bg='red')
        self.LeftFrame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.MiddleFrame = tk.Frame(root)
        self.MiddleFrame.pack(side=tk.LEFT, pady=5, expand=False, fill=tk.Y)

        self.RightFrame = tk.Frame(root, bg='blue')
        self.RightFrame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.Separator = ttk.Separator(self.MiddleFrame, orient=tk.VERTICAL)
        self.Separator.pack(side=tk.LEFT, padx=5, pady=5, expand=False, fill=tk.Y)

        self.ActiveSaveBox = tk.Frame(self.LeftFrame, bg='orange')
        self.ActiveSaveBox.pack(side=tk.TOP, padx=5, pady=5, ipady=20, expand=False, fill=tk.NONE)

        self.ActiveSaveText = tk.Label(self.ActiveSaveBox, bg='yellow', text="Configuring ...")
        self.ActiveSaveText.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.Separator2 = ttk.Separator(self.LeftFrame, orient=tk.HORIZONTAL)
        self.Separator2.pack(side=tk.TOP, padx=5, pady=5, expand=False, fill=tk.X)

        self.SaveOrgBox = tk.Frame(self.LeftFrame, bg='orange')
        self.SaveOrgBox.pack(side=tk.TOP, expand=False, fill=tk.X)

        self.NewSaveButton = tk.Button(self.SaveOrgBox, text="+ New Save")
        self.NewSaveButton.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        self.SavesSortDropdown = ttk.Combobox(self.SaveOrgBox, values=C2SaveManager_support.SaveOrganisationOptions)
        self.SavesSortDropdown.set(C2SaveManager_support.SaveOrganisationOptions[0])
        self.SavesSortDropdown.pack(side=tk.RIGHT, padx=5, pady=5, expand=True, fill=tk.X)

        self.SavesBox = ttk.Treeview(self.LeftFrame)
        self.SavesBox.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.ActivateButton = tk.Button(self.RightFrame, text="Activate", state=tk.DISABLED)
        self.ActivateButton.pack(side=tk.BOTTOM, padx=5, pady=5, ipady=10, expand=False, fill=tk.X)

        self.SelectedSaveName = tk.Label(self.RightFrame, text="Configuring ...")
        self.SelectedSaveName.pack(side=tk.TOP, padx=5, pady=5, ipady=5, expand=False, fill=tk.X)

class Toplevel2:
    def __init__(self, top=None):
        global SecondStepFramePack

        top.title("First Setup Configure")
        self.top = top
        root = self.top

        self.FirstStepFrame = tk.Frame(root, bg='green')
        self.FirstStepFrame.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.Label1 = tk.Label(self.FirstStepFrame, text="Crew 2 Folder")
        self.Label1.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        self.folderinputframe = tk.Frame(self.FirstStepFrame, bg='lime')
        self.folderinputframe.pack(side=tk.TOP, expand=False, fill=tk.X)

        self.FolderInput = tk.Entry(self.folderinputframe)
        self.FolderInput.pack(side=tk.LEFT, padx=5, pady=5, ipadx=200, ipady=2, expand=True, fill=tk.X)

        self.folderbrowsebutton = tk.Button(self.folderinputframe, text="Browse")
        self.folderbrowsebutton.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=10, ipady=2, expand=False, fill=tk.X)

        self.Seperator = ttk.Separator(self.FirstStepFrame, orient=tk.HORIZONTAL)
        self.Seperator.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        self.Label2 = tk.Label(self.FirstStepFrame, text="Crew 2 EXE (Optional)")
        self.Label2.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        self.exeinputframe = tk.Frame(self.FirstStepFrame, bg='lime')
        self.exeinputframe.pack(side=tk.TOP, expand=False, fill=tk.X)

        self.exeinput = tk.Entry(self.exeinputframe)
        self.exeinput.pack(side=tk.LEFT, padx=5, pady=5, ipadx=200, ipady=2, expand=True, fill=tk.X)

        self.exebrowsebutton = tk.Button(self.exeinputframe, text="Browse")
        self.exebrowsebutton.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=10, ipady=2, expand=False, fill=tk.X)

        self.sep2 = ttk.Separator(self.FirstStepFrame, orient=tk.HORIZONTAL)
        self.sep2.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        self.continuebutton = tk.Button(self.FirstStepFrame, text="Continue", command=C2SaveManager_support.SwapToStep2)#, state=tk.DISABLED
        self.continuebutton.pack(side=tk.TOP, padx=5, pady=5, ipadx=10, ipady=3, expand=False)

        self.SecondStepFrame = tk.Frame(root, bg='yellow')
        self.SecondStepFrame.pack(side= tk.TOP,padx= 5,pady= 5,expand= True,fill= tk.BOTH)
        self.SecondStepFrame.pack_forget()

        self.Label3 = tk.Label(self.SecondStepFrame, text='''Offline Save Detected!
Please Enter a name for this save''')
        self.Label3.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        #self.nameinputframe = tk.Frame(self.SecondStepFrame, bg='greenyellow')
        #self.nameinputframe.pack(side=tk.TOP, expand=False, fill=tk.X)

        self.nameinput = tk.Entry(self.SecondStepFrame)
        self.nameinput.pack(side=tk.TOP, padx=5, pady=5, ipadx=200, ipady=2, expand=True, fill=tk.X)
        
        self.sep3 = ttk.Separator(self.SecondStepFrame, orient=tk.HORIZONTAL)
        self.sep3.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.X)

        self.submitbutton = tk.Button(self.SecondStepFrame, text="Submit")#, state=tk.DISABLED
        self.submitbutton.pack(side=tk.TOP, padx=5, pady=5, ipadx=10, ipady=3, expand=False)
        
def start_up():
    C2SaveManager_support.main()

if __name__ == '__main__':
    C2SaveManager_support.main()




