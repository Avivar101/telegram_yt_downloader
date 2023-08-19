from pytube import YouTube

# create a new YouTube instance
def create_yt(url):
    yt = YouTube(url)

    return yt

# return yt_video selection info
def resolution_picker(yt):
    streams = yt.streams
    resolutions = list(set([stream.resolution for stream in streams]))
    print("resolutions returned...")
    
    return resolutions

# download video
def download_video(res, yt):
    video_stream = yt.streams.filter(progressive=True, res=res, file_extension='mp4').first()
    video_stream.download()

