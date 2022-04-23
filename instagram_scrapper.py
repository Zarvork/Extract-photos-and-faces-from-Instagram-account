from selenium import webdriver
import time
import os
import cv2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#This function allows you to connect to your Instagram account using Selenium
def login_instagram(username,password):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
    browser.set_window_size(1366, 768)
    browser.get("https://www.instagram.com")
    browser.find_element_by_class_name("bIiDR").click()
    time.sleep(3)
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_class_name("L3NKy").click()
    time.sleep(3)
    return browser
#This function allows you to download the first 24 photos of the selected Instagram account
def get_photos(account_name):
    width = 640
    height = 640
    i=0
    browser.get("https://www.instagram.com/"+account_name)
    time.sleep(3)
    os.mkdir(account_name)
    list_image = browser.find_elements(By.CSS_SELECTOR, 'img.FFVAD')
    for image in list_image:
        i=i+1
        url_image = image.get_attribute("src")
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get(url_image)
        browser.set_window_size(width,height)
        browser.save_screenshot("./"+account_name+"/"+account_name+"_"+str(i)+".png")
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
#This function allows to extract the faces found in the photos downloaded with get_photos using OpenCV
def extract_faces(path):
    os.mkdir(path+"/"+"faces")
    list_of_files = os.listdir(path)
    for file in list_of_files:
        if file.endswith(".png"):
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
            image = cv2.imread(path+"/"+file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            face = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=4,
            minSize=(30, 30),
            )
            for x, y, w, h in face:
                cv2.imwrite(path+"/"+"faces/"+file.replace(".png","")+"_face"+".png", image[y:y+h, x:x+w])
