FROM python:3.6-alpine

RUN adduser -D desafioSurfMappers

WORKDIR /home/desafioSurfMappers

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY galeriasm galeriasm
COPY migrations migrations
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R desafioSurfMappers:desafioSurfMappers ./
USER desafioSurfMappers

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
