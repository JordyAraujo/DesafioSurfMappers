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
RUN printf 'AWS_ACCESS_KEY_ID = "AKIA5VIHLDO3PDEYTTZP"\nAWS_SECRET_ACCESS_KEY = "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"\nBUCKET = "galeriasmbucket"\nAWS_REGION_NAME = "sa-east-1"' > .secrets.py

ENV FLASK_APP run.py

RUN chown -R desafioSurfMappers:desafioSurfMappers ./
USER desafioSurfMappers

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]