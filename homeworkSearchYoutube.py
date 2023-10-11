import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com")

searchBox = driver.find_element(By.NAME, "search_query")
searchBox.clear()
searchBox.send_keys("project LA")
searchBox.send_keys(Keys.ENTER)


firstVideo = driver.find_element(By.XPATH, "//ytd-video-renderer[@class='style-scope ytd-item-section-renderer'][1]")
firstVideo.click()
time.sleep(30)

pause_button = driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button'][1]")
pause_button.click()
time.sleep(5)


searchBox.clear()
driver.quit()
