# The Crew 2 Offline Save Manager
> [!Note]
> Functionality described hasn't been implemented yet but is on the feature plan

> [!Important]
> This project dose not feature AI in any aspect  
> You can view Development files in the "Dev Files" folder

Crew2 Offline Save Manager is an external program made in python program that lets you manage multiple offline save files. Even if the program is removed all the save files are still accessible.

### Usage
Download the Release and either run the **.EXE** or **.PY** (Both do the same thing so it is your choice).

On first launch it will attempt to auto detect your `The Crew 2` Folder in your documents if not you will need to enter it manually alongside that you may enter the location of your `Crew2.exe` for ease of access.  
After if it detects an existing offline save then it will prompt you to enter a name to setup the existing offline save.

On the left hand side it shows all of your offline saves with your active save at the top. Clicking on these (including the active save) shows details about that specific save on the right hand side.  
On the right hand side at the bottom there are options to edit you offline save (Inactive saves only).

For the Inactive saves:  
- Clicking Activate sets that save as active ready for play

For the Active save:
- If you have configured your Crew2.exe then you can hit play and it will launch. (It is still through steam so controller support and other adjustments will still work)

### Details
It works by moving the `main-save.bin` to and from `Documents\The Crew 2\Save\[Your User ID]\` & `Documents\The Crew 2\SaveManager Saves\[Save Name]\` depending on which save file you have active.

When swapping saves around it will copy from the main save folder into its savemanager save folder and then check the copy matches before removing the active save (The same happens when setting the active save). If there is an issue with any point in this process then it will give the error:
```
Critical Error:
Migrating Saves Not Safe | 0
```
`1 ▶ Issue Moving active save offline`  
`2 ▶ Issue Moving offline save to active`

The program gets the information: `Follower Count` `Amount of Bucks` `Total Playtime` from reading the `main-save.bin`  
While: `Save Name` `Date last played` `Preview screenshot` are saved alongside in the `\SaveManager Saves\[Save Name]\` in `SaveManagerData.xml`

### Credits
[PAGE](https://page.sourceforge.net/) for the formatting of the *main* and *_Support* scripts (Dev Files ▶ 01b and newer files)  
[TC2SaveExtractor](https://github.com/Telonof/TC2SaveExtractor) for allowing me to reverse engineer the bytes for save file previews
