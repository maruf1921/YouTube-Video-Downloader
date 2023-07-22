import pytube

playlist_url = input("Enter the link :")
play_list = pytube.Playlist(playlist_url)
#video_stream = youtube_object.streams.get_highest_resolution()

print(play_list.title)

for video in play_list.videos:
    video_stream = video.streams.filter(res="720p").first()
    video_stream.download()

print("*** Download Successfully ***")