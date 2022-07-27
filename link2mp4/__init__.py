try:
    from . import youtube, reddit, twitter, tiktok, vimeo, twitch, veoh
except ImportError:
    import youtube, reddit, twitter, tiktok, vimeo, twitch, veoh
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download,
    'TikTok': tiktok.download,
    'Vimeo': vimeo.download,
    'Twitch': twitch.download,
    'Veoh': veoh.download,
}