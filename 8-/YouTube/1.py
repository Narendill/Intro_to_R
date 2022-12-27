from pytube import YouTube
import os

os.system('CLS')

link = 'https://www.youtube.com/watch?v=RrQ3p4QI-mQ'


f = YouTube(link)

for i in f.streams:
    print(i)
    print('###')

f.streams.first().download()
YouTube(link).streams.get_highest_resolution().download()