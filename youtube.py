#import pytube library to download the video
import pytube

#Ask for the url of video
url = input("Enter video url")
#we can take path as well, just comment the following line
#path = input("Enter the path of storage")

#specify the storage path of video
path="E:"

#magic line to download the video
pytube.Youtube(url).streams.get_highest_resolution().download(path)

#clcoding.com
