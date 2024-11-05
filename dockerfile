FROM python:3-slim

RUN apt update && sudo apt upgrade
RUN apt install ffmpeg

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]