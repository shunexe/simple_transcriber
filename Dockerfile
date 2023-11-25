FROM python:3.11-bookworm

#REF:https://github.com/openai/whisper
RUN apt update && apt install -y ffmpeg

RUN pip install git+https://github.com/openai/whisper.git
