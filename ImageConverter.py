import PySimpleGUI as sg
import os.path
import subprocess
import threading
from pathlib import Path
from PIL import Image
from PIL import GifImagePlugin
from playsound import playsound

#---------------GUI LAYOUT---------------
sg.theme('Default1')
# First column layout
file_list_column = [
    [sg.Text("Image Folder"), sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),sg.FolderBrowse(),],
    [sg.Listbox(values=[], enable_events=True, size=(40,20), key="-FILE LIST-")],
]

# Second column layout
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left.")],
    [sg.Text(size=(40,1), key="-TOUT-")], #Return debug text field
    [sg.Text("Convert to...")],
    [sg.Combo(('Compress for Discord', 'Deep Fried'), enable_events=True, key="-CONVERTCHOICE-", size=(20, 1)),],
    [sg.Button("CONVERT", key="-CONVERTERBUTTON-", disabled=True)],
]

# FULL LAYOUT
layout = [
    [sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column),]
]

# Get the screen size and create usable values
w, h = sg.Window.get_screen_size()
window = sg.Window("Image Converter", layout, resizable=False).Finalize()
halfSizeXstr = w/2.5
halfSizeYstr = h/2.5
halfSizeX = int(halfSizeXstr)
halfSizeY = int(halfSizeYstr)

# Main window sizing
window.TKroot.minsize(halfSizeX,halfSizeY)
window.TKroot.maxsize(halfSizeX,halfSizeY)

#-------------METHODS-------------
def error_popup():
    playsound('failure.wav')
    
def success_popup():
    playsound('success.wav')

#---------------LOGIC---------------
# Event loop
while True:    
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # folder name was filled in, so make a list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
            
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)

    if event == "-FILE LIST-": # a file was chosen from the list
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-CONVERTERBUTTON-"].update(disabled=False)
        except:
            pass

    if event == "-CONVERTERBUTTON-" and values["-CONVERTCHOICE-"] == '':
        threads = []
        t = threading.Thread(target=error_popup)
        t.start()
        sg.Popup('Please select an output format')
        
    if event == "-CONVERTERBUTTON-" and values["-CONVERTCHOICE-"] == 'Compress for Discord':
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save("DiscordCompressed.jpg", quality=25)
        
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
            
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
        
        cwd = os.getcwd()
        threads = []
        t = threading.Thread(target=success_popup)
        t.start()
        sg.Popup('Done!', 'Saved to: {0}'.format(cwd))
        subprocess.Popen(r'explorer /select, "{0}"'.format(cwd))

    if event == "-CONVERTERBUTTON-" and values["-CONVERTCHOICE-"] == 'Deep Fried':
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save("DeepFried.jpg", quality=3)
        
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
            
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
        
        cwd = os.getcwd()
        threads = []
        t = threading.Thread(target=success_popup)
        t.start()
        sg.Popup('Done!', 'Saved to: {0}'.format(cwd))
        subprocess.Popen(r'explorer /select, "{0}"'.format(cwd))
        
window.close()