import sys
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.constants import *
from pathlib import Path
import ctypes.wintypes
import xml.etree.ElementTree as ET

import C2SaveManager

SaveOrganisationOptions = ["Most Recent Played", "Least Recent Played", "Alphabetical (A-Z)", "Alphabetical (Z-A)", "Time Played (Highest)", "Time Played (Lowest)"]


def main(*args):
    MainLaunch()

if __name__ == '__main__':
    C2SaveManager.start_up()

#def FirstStartLaunch():
    

#def MainPrecheck():
    #Using the XML file check if the Crew Folder and EXE are good

def MainLaunch():

    WhichOne = True

    if WhichOne:
        LaunchMainGUI()
    else:
        LaunchFirstGUI()
    #Launches the main gui & populates it

def LaunchMainGUI():

    global MainGUIRoot
    global _top1, _w1

    global FirstLaunchGUIRoot
    global _top2, _w2

    MainGUIRoot = tk.Tk()
    MainGUIRoot.protocol( 'WM_DELETE_WINDOW' , MainGUIRoot.destroy)
    _top1 = MainGUIRoot
    _w1 = C2SaveManager.Toplevel1(_top1)

    DoFirstLaunch = False

    if DoFirstLaunch:
        FirstLaunchGUIRoot = tk.Toplevel(MainGUIRoot)
        _top2 = FirstLaunchGUIRoot
        _w2 = C2SaveManager.Toplevel2(_top2)

    MainGUIRoot.mainloop()

def LaunchFirstGUI():

    global FirstLaunchGUIRoot
    global _top2, _w2

    #FirstLaunchGUIRoot = tk.Toplevel()
    #FirstLaunchGUIRoot.protocol( 'WM_DELETE_WINDOW' , FirstLaunchGUIRoot.destroy)
    #_top2 = FirstLaunchGUIRoot
    #_w2 = C2SaveManager.Toplevel1(_top2)

    #FirstLaunchGUIRoot.mainloop()
