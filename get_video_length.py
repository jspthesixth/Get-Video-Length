import os
import datetime
from moviepy.video.io.VideoFileClip import VideoFileClip

# THIS FILE SHOULD BE IN THE SAME DIRECTORY AS YOUR VIDEO FILES
# IF NOT, ASSIGN FULL PATH OF THE VIDEO FILES TO directory VARIABLE
# directory = '/path/to/the/videos'
directory = os.listdir(os.getcwd())

# ADD MORE VIDEO FORMATS TO THIS LIST IF YOU NEED
supported_video_formats = ["avi", "flv", "wmv", "mp4"]
videos = []
video_lengths = []

for video in directory:
    root, ext = os.path.splitext(video)
    if ext[1:] in supported_video_formats:
        videos.append(root)
        clip = VideoFileClip(video)
        length = clip.duration
        clip.close()
        video_lengths.append(length)

if len(videos) == 0:
    print("There is no video files in the current directory!")
else:
    info = dict(zip(videos, video_lengths))
    sorted_info = {k: v for k, v in sorted(info.items(), key=lambda item: item[1])}
    for k, v in sorted_info.items():
        print(k, "==>", datetime.timedelta(seconds=v))
