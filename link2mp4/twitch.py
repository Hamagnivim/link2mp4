try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    try:
        return video(list(filter(lambda req: '.mp4' in req, requests('https://www.twitch.tv/%s' % input('https://www.twitch.tv/'))))[0])
    except IndexError:
        raise BaseException('This is only for clips not streams or videos. Try again.')