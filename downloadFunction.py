import youtube_dl

#Given a Youtube link, download the result
def download(link):
    ydl_opts = {'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return True

#Give a list of youtube links, download all of the results
def downloadList(list, n):
    count = 0
    for link in list:
        download(link)
        count = count + 1
        if count > n:
            break
    return True

#Give a list of youtube links, download all of the results
def downloadList(youtubeList):
    for link in youtubeList:
        download(link)
    return True

def downloadTwo(link, name):
    ydl_opts = {'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    return True
