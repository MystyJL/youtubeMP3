import os
import shutil
import yt_dlp

def mp3Convert(video="", path_for_song=""):
    if video == "":
        return
    if path_for_song == "" or path_for_song==None:
        return
    # configs
    ydl_opts = {"playliststart":1,
                "ignoreerrors":True,
        'format': 'bestaudio/best',
                'outtmpl': u'%(title)s.%(ext)s',
                'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256',
        }]}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])
# move to desired folder
    after = [x for x in os.listdir(os.getcwd())]
    for file_name in after:
        # construct full file path
        source = file_name
        destination = path_for_song+ "/"+file_name
        # move only files
        if file_name[-3:]=="mp3":
            shutil.move(source, destination)
