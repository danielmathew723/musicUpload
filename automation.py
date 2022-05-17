import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ip = 'https://getmusic.cc/'  # asks for ip address
code = input('Enter validation code: ')
url = input('Enter video URL: ')  # asks for video url

# need to make a service object because it throws error otherwise
s = Service('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')

# change current working directory to Downloads folder to check for my file
directory = 'C:/Users/drmat/Downloads/'
os.chdir(directory)

convert_driver = webdriver.Chrome(service=s)

# driver accesses Google Chrome and opens website
convert_driver.get('https://onlinevideoconverter.pro/en20/youtube-converter-mp3')

# asks for url as input and enters URL into search bar
search = convert_driver.find_element(By.ID, "texturl")
search.send_keys(url)
enter = convert_driver.find_element(By.ID, "convert1")
enter.click()

# wait for title text to change and retrieves song title
time.sleep(7)
title = convert_driver.find_element(By.ID, "result_title").text
print('title retrieved')

time.sleep(5)
# finds and clicks the download button after it appears
try:
    download = convert_driver.find_element(By.ID, "download-720-MP4")
    download.click()
except selenium.common.exceptions.NoSuchElementException:
    download = convert_driver.find_element(By.ID, "download-360-MP4")
    download.click()

# checks my Downloads folder to see if song is downloaded
song_file = title + '.mp3'
is_downloaded = False
while not is_downloaded:
    downloads = os.listdir()
    if song_file in downloads:
        is_downloaded = True
        print('downloaded')
    else:
        continue

convert_driver.quit()

# opens offline app download site
music_driver = webdriver.Chrome(service=s)
music_driver.get(ip)

code_1 = music_driver.find_element(By.ID, "tab1")
code_2 = music_driver.find_element(By.ID, "tab2")
code_3 = music_driver.find_element(By.ID, "tab3")
code_4 = music_driver.find_element(By.ID, "tab4")

code_1.send_keys(code[0])
code_2.send_keys(code[1])
code_3.send_keys(code[2])
code_4.send_keys(code[3])

time.sleep(7)

# sends file path to upload element and uploads song
file_path = directory + song_file
upload = music_driver.find_element(By.ID, 'fileupload')
upload.send_keys(file_path)

# waits for upload to finish (should find more optimal method)
time.sleep(10)

music_driver.quit()

# TODO
# learn how to use expected_conditions and WebDriverWait
# turn into functions to compartmentalize functionality
