from seleniumwire.webdriver import Firefox, Chrome, Edge, Safari
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from urllib3 import PoolManager
DEBUG = False # change to make the browser visible for debugging
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
        options.headless = not DEBUG
        options.mute_audio = True
        browsers[browser](options=options)
    except:
        continue
    break
else:
    raise Exception("No browser found, please install geckodriver")
def requests(url, click_on=None):
    driver = browsers[browser](options=options)
    driver.get(url)
    if click_on:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, click_on)))
        driver.find_element_by_xpath(click_on).click()
        while not len(list(filter(lambda req: '.mp4' in req.url, driver.requests))):
            sleep(.1)
    requests = driver.requests
    driver.quit()
    return list(map(lambda req: req.url, requests))
def video(video, audio=None):
    if audio is None:
        return PoolManager().request('GET', video).data
    else:
        return video, audio