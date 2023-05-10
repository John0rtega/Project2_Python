from pytube import YouTube
from sys import argv

print('''Welcome!
In this program you can download any YouTube video! 
''')

# Get the link from the command line
link = argv[1]
yt = YouTube(link)

# Print the title of the YouTube video
print("Title: ", yt.title)

# Print number of views 
print("View ", yt.views)

# Get highest resolution of the video
downloadVideo = yt.streams.get_highest_resolution()

# Download the video
download = downloadVideo.download('/Users/jaof0/OneDrive/Desktop/Downloaded Videos/')
print(download)

# Print message when download is complete
if(download):
    print("Done.")

# https://youtu.be/u3V5KDHRQvk