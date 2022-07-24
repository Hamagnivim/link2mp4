try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://vimeo.com/')
    req = requests('https://vimeo.com/%s' % id, click_on='//button[contains(@class, "play")]')
    vid = list(filter(lambda req: '.mp4' in req and '/audio/' not in req, req))[0]
    try:
        aud = list(filter(lambda req: '.mp4' in req and '/audio/' in req, req))[0]
        aud = aud[:aud.rfind('?')]
    except IndexError:
        aud = None
    return video(vid[:vid.rfind('?')], aud)