from moviepy.editor import *

mp4_file = r".mp4" # made support for .crdownload files too
mp3_file = r".mp3"

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()

# Put the song name in front of the .mp4 and .mp3 
# (.crdownload optional)
# After doing it, go the the file directory like this
# C:\User\Hp\Desktop\Python Video Editor\src\main.py
# write "python main.py" in the command prompt.
# after that, the mp3 version of the file can be 
# found in the src folder