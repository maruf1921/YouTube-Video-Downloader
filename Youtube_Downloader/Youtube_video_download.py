import pytube

video_url = input("Enter the link :")
youtube_object = pytube.YouTube(video_url)
#video_stream = youtube_object.streams.get_highest_resolution()

print(youtube_object.title)
video_stream = youtube_object.streams.all()
lst = list(enumerate(video_stream))
for i in lst:
    print(i)
print()
strm = int(input("Enter which resulotion :"))
video_stream[strm].download()
print("*** Download Successfully ***")