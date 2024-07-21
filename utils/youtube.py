
import string, random, yt_dlp

class Download():
    def __init__(self, url = None):
        if url is None or url == '':
            url = input('Укажи ссылку: ')

        self.filename = f'{self.generate_name(10)}.mp4'
        self.url = url

    def download_youtube_video(self):
        ydl_opts = {
            'outtmpl': f'utils/video/{self.filename}',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

        return self.filename

    @staticmethod
    def generate_name(len):
        return ''.join(random.choice([i for i in (string.ascii_letters + '1234567890')]) for i in range(len))










