# Extract-photos-and-faces-from-Instagram-account
This project uses Selenium and OpenCV. It requires that you install chromedriver to use Selenium (https://chromedriver.chromium.org/).

This project is made of a python file (instagram_scrapper.py) which contains three functions : login_instagram(), get_photos and extract_faces().

login_instagram() takes your Instagram user name and password as parameters. This function allows you to connect to your Instagram account using Selenium and ChromeDriver. It is this function that you should call first.

Then, you need to call the get_photos() function which allows you to download at most the first 24 photos of the chosen Instagram account. It takes the name of the Instagram account as a parameter.

The function extract_faces() allows to extract the faces of the previously downloaded photos by using OpenCV. It takes as parameter the path of the folder containing the photos
