try:
    from . import youtube, reddit, twitter, pinterest, tiktok, vimeo, twitch
except ImportError:
    import youtube, reddit, twitter, pinterest, tiktok, vimeo, twitch
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download,
    'Pinterest': pinterest.download,
    'TikTok': tiktok.download,
    'Vimeo': vimeo.download,
    'Twitch': twitch.download
}