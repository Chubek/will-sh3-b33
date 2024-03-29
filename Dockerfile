FROM python:latest

WORKDIR /home/willshebe

COPY . ./

RUN chmod +x boot.sh

RUN apt-get update && apt-get install build-essential wget libsvm-dev ffmpeg libsm6 libxext6 -y

RUN pip install --no-cache-dir -r req-main.txt
RUN pip install --no-cache-dir -r req-sklearn.txt
RUN pip install --no-cache-dir -r req-server.txt


RUN wget https://cdn.discordapp.com/attachments/797919965264085092/889497440179343360/env

ENTRYPOINT ["./boot.sh"]
