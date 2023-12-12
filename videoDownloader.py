from pytube import YouTube

def DownloadVideo(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ocorreu um erro.")
    print("Download concluido com sucesso!")


link = input("Digite a URL do video do Youtube: ")
DownloadVideo(link)