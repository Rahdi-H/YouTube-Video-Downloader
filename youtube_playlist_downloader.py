from pytube import Playlist

py = Playlist("##")
print(f'Downloading : {py.title}')
for video in py.videos:
    video.streams.first().download()