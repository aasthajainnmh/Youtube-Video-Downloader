from selenium import webdriver
import youtube_dl 
import time
import os
url = input("Enter the Youtube Playlist URL : ")
driver = webdriver.Chrome() 
driver.get(url)
time.sleep(5)
playlist=[]
videos=driver.find_elements_by_class_name('style-scope ytd-playlist-video-renderer')

for video in videos:
    link=video.find_element_by_xpath('.//*[@id="content"]/a').get_attribute("href")
    end=link.find("&")
    link=link[:end]
    playlist.append(link)


os.chdir('C:/Users/Trideep/Downloads') 

for link in playlist:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
driver.close()