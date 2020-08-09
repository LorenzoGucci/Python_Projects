from pytube import YouTube

# Video = YouTube(input('Insert the url of the video you want to download here:\n'))
# print('\tTitle: ', Video.title, '\n', '\tRating: ', Video.rating)
Video = YouTube('https://www.youtube.com/watch?v=OXQ89_8UOfw')
print('\tTitle: ', Video.title, '\n', '\tRating: ', Video.rating)
# Video = Video.get('mp4', '720p')
Video.streams.first().download(input('Insert save path here:\n'))
