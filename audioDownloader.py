from pytube import YouTube

def DownlaodAudio(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download()
    except:
        print("Ocorreu um erro.")
    print("Download concluido com sucesso")


link = input("Digite a URL do video do Youtube: ")
DownlaodAudio(link)