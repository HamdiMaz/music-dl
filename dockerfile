FROM python:3-slim

EXPOSE 8118

RUN apt-get update && apt-get upgrade -y
RUN apt install ffmpeg -y

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]