from pytube import YouTube
from pytube.cli import on_progress

print("Starting")

url = "https://www.youtube.com/watch?v=w5zvh6UThwE"
videox = YouTube(url)
# videox = YouTube(url, on_complete_callback=on_progress)   <- This will add a progress bar when downloading

# Get Video title
print(f'VIDEO TITLE: {videox.title}')

# Get thumbnail image URL
print(f'THUMBNAIL IMAGE URL: {videox.thumbnail_url}')

# Download the youtube video
# 1st: Set the stream resolution
# Set video to highest resolution
videox = videox.streams.get_highest_resolution()  # OR videoX = videoX.streams.first()

# To get list of all resolutions for the video
#for stream in videox.streams.first:
#    print(stream)

# Download the youtube  video
videox.download()
