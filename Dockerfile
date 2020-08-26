from python:3.7-buster
RUN apt-get update && apt-get install vim -y --no-install-recommends

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/DjangoDownloader
RUN mkdir -p /opt/app/YoutubeScripts

COPY DjangoDownloader /opt/app/DjangoDownloader
COPY YoutubeScripts /opt/app/YoutubeScripts
RUN chmod -R 775 /opt/app

WORKDIR /opt/app/YoutubeScripts
RUN pip3 install -r requirements.txt --cache-dir /opt/app/YoutubeScripts/.pip_cache
WORKDIR /opt/app/DjangoDownloader
RUN pip3 install -r requirements.txt --cache-dir /opt/app/DjangoDownloader/.pip_cache

EXPOSE 8080
STOPSIGNAL SIGTERM
ENTRYPOINT ["python3", "/opt/app/DjangoDownloader/app.py"]
