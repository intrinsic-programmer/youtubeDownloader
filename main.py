from pytube import YouTube

link = input("Enter Link of Youtube Video: ")
yt = YouTube(link)

print("Title :", yt.title)
print("Views :", yt.views)
print("Duration :", yt.length,"seconds")
print("Description :", yt.description)
print("Ratings :", yt.rating)
authorize=input("Do You Want To Download write yes / no ")
if(authorize=="yes"):
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!!")
else:
    print("Okay Not Downloading")
