from moviepy.editor import VideoFileClip, AudioFileClip
from seleniumwire.webdriver import Firefox, Chrome, Edge, Safari
Options = lambda: None # noqa
browsers = {
    'firefox': Firefox,
    'chrome': Chrome,
    'edge': Edge,
    'safari': Safari
}
for browser in browsers:
    try:
        exec("from selenium.webdriver.%s.webdriver import Options" % browser)
        options = Options()
        options.headless = True
        browsers[browser](options=options)
    except:
        pass
    else:
        break
def requests(url):
    driver = browsers[browser](options=options)
    driver.get(url)
    requests = driver.requests
    driver.quit()
    return list(map(lambda req: req.url, requests))
def video(video, audio=None):
    if audio is None:
        return VideoFileClip(video)
    else:
        return VideoFileClip(video).set_audio(AudioFileClip(audio))