try:
    from . import youtube, reddit, twitter, pinterest
except ImportError:
    import youtube, reddit, twitter, pinterest
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download,
    'Pinterest': pinterest.download
}