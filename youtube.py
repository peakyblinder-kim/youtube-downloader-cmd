import pytube
url = input("Enter video url")
path="E:"
pytube.Youtube(url).streams.get_highest_resolution().download(path)

