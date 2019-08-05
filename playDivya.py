import time

from moviepy.editor import VideoFileClip


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def open_page():
    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com/divyamsodhi/')
    return browser

def click_on_first_video(browser):
    firstThumbnail = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_bz0w"))
    )
    firstThumbnail.click()

def getVideoURL():
    time.sleep(0.5)
    videoTag = browser.find_element_by_css_selector('video')
    videoURL = videoTag.get_attribute("src")
    return videoURL

def getVideoDuration(videoURL):
    clip = VideoFileClip(videoURL)
    return clip.duration


def loop_through_videos():
    for i in range(10):

        videoURL = getVideoURL()
        videoDuration = getVideoDuration(videoURL)

        print("videoURL: %s" % videoURL)
        print("videoDuration: %s" % videoDuration)

        playBtn = WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "OAXCp"))
        )
        playBtn.click()

        time.sleep(videoDuration)

        nextBtn = WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "coreSpriteRightPaginationArrow"))
        )
        nextBtn.click()


if __name__ == "__main__":
    browser = open_page()
    click_on_first_video(browser=browser)
    loop_through_videos()