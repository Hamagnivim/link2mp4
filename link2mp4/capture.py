from moviepy.editor import VideoFileClip, AudioFileClip
from seleniumwire.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import Options
firefox_options = Options()
firefox_options.headless = True
def requests(url):
    driver = Firefox(options=firefox_options)
    driver.get(url)
    requests = driver.requests
    driver.quit()
    return list(map(lambda req: req.url, requests))
def video(video, audio=None):
    if audio is None:
        return VideoFileClip(video)
    else:
        return VideoFileClip(video).set_audio(AudioFileClip(audio))