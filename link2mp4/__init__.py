try:
    from . import youtube, reddit, twitter, pinterest, tiktok, vimeo
except ImportError:
    import youtube, reddit, twitter, pinterest, tiktok, vimeo
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download,
    'Pinterest': pinterest.download,
    'TikTok': tiktok.download,
    'Vimeo': vimeo.download
}