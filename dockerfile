
FROM python:latest

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /root/yt_downloader/

COPY . .

RUN pip install -r requirements.txt

CMD [ "bash", "-c", "python bot.py" ]
