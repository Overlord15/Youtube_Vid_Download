'''
YouTube Video Downloader
Author: Code With AK
'''
import os  
from pytube import YouTube

# Your URL goes here

url = input("Enter the full video url :: ") 
my_video = YouTube(url)

print("\nVideo Title ⤵\n")

#get Video Title
print(my_video.title)

print("\nTumbnail Image ⤵\n")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("\nDownload video ⤵\n")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#or
#my_video = my_video.streams.first()

#Download video
my_video.download()


