try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download(): # TODO: implement
    id = input('Enter Twitter video ID')
    return video(video=None, audio=None) # returns a video from a video url and an **optional** audio url