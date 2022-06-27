try:
    from . import youtube, reddit, twitter
except ImportError:
    import youtube, reddit, twitter
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download
}