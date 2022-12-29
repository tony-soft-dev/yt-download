from pytube import YouTube
from sys import argv
from pytube.cli import on_progress

link = input("Enter YouTube URL you wish to download: ")
yt = YouTube(link, on_progress_callback=on_progress)

print("Preparing to download: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download('./YTfolder')

print("--> ")