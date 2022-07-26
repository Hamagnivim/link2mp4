try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://www.veoh.com/watch/')
    req = requests('https://www.veoh.com/watch/%s' % id)
    vid = list(filter(lambda req: '.mp4?e' in req, req))[0]
    return video(vid)