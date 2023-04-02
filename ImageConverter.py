import os
import PySimpleGUI as sg
from PIL import Image
import moviepy.editor as mp

# Create a layout for the GUI
layout = [[sg.Text('Select a file to compress:')],
          [sg.Input(key='file'), sg.FileBrowse()],
          [sg.Text('Select compression level:')],
          [sg.Slider(range=(0, 100), default_value=50, orientation='h', key='compression')],
          [sg.Text('Select file type:')],
          [sg.DropDown(values=('jpg', 'png', 'mp4'), default_value='jpg', key='file_type')],
          [sg.Button('Compress'), sg.Exit()]]

# Create a window and display the GUI
window = sg.Window('File Compression Tool', layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    file_path = values['file']
    file_type = values['file_type']
    compression_level = int(values['compression'])

    # Check if selected file format matches the file format of the input
    if file_type != os.path.splitext(file_path)[1][1:]:
        sg.Popup(f'Selected file type does not match the file format of the input!')
        continue

    # Compress image files
    if file_type in ('jpg', 'png'):
        with Image.open(file_path) as img:
            filename, ext = os.path.splitext(file_path)
            compressed_file_path = f'{filename}_compressed.{ext}'
            img.save(compressed_file_path, optimize=True, quality=(100-compression_level))

        sg.Popup(f'File compressed successfully! Saved as {compressed_file_path}')

    # Compress video files
    elif file_type == 'mp4':
        clip = mp.VideoFileClip(file_path)
        filename, ext = os.path.splitext(file_path)
        compressed_file_path = f'{filename}_compressed.{ext}'
        clip.write_videofile(compressed_file_path, codec='libx264', bitrate=f'{compression_level}k')

        sg.Popup(f'File compressed successfully! Saved as {compressed_file_path}')

window.Close()
