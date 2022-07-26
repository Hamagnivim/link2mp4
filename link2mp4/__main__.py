import ffmpeg
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from questionary import select
from os import remove
try:
    from . import download_functions
except ImportError:
    from __init__ import download_functions
def main():
    Tk().withdraw()
    outname = asksaveasfilename(filetypes = [("MP4 file", "*.mp4")])
    if outname == '':
        return
    if not outname.endswith('.mp4'):
        outname += '.mp4'
    website = select("Choose source website", download_functions.keys()).ask()
    try:
        video = download_functions[website]()
        if isinstance(video, bytes):
            open(outname, 'wb').write(video)
        elif isinstance(video, tuple):
            try:
                remove(outname)
            except FileNotFoundError:
                pass
            ffmpeg.output(ffmpeg.input(video[0]), ffmpeg.input(video[1]), outname).run()
    except KeyboardInterrupt:
        print('\nCancelled.')
if __name__ == '__main__': main()