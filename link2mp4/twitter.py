from urllib.parse import urlparse
from requests import get
from m3u8 import loads
try:
    from .capture import requests
except ImportError:
    from capture import requests
def download():
    id = input('https://twitter.com/')
    req = requests('https://twitter.com/%s' % id)
    playlist_source = list(filter(lambda req: '.m3u8' in req, req.copy()))[0]
    host = urlparse(playlist_source)
    host_url = '%s://%s' % (host.scheme, host.hostname)
    playlists_text = get(playlist_source).text
    playlists = loads(playlists_text)
    if playlists.playlists:
        playlists_text = get(host_url + max(playlists.playlists, key=lambda x: x.stream_info.resolution).uri).text
        playlists = loads(playlists_text)
    return get(host_url + playlists_text[playlists_text.find('"') + 1: playlists_text.rfind('"')]).content + b''.join(map(lambda x: get(host_url + x).content, playlists.segments.uri))