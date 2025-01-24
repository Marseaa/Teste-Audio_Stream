FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_PREFER_BINARY=1 \
    CUDA_HOME=/usr/local/cuda-11.8 \
    TORCH_CUDA_ARCH_LIST="8.6"

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y wget
RUN apt-get install -y python3  && apt-get install -y python3-pip
RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

RUN pip install torch torchvision torchaudio transformers 
#RUN pip install --force-reinstall "faster-whisper @ https://github.com/SYSTRAN/faster-whisper/archive/refs/heads/master.tar.gz" && \
RUN pip install numpy==1.24.3
RUN pip install transformers
RUN pip install scipy

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN apt-get install gcc -y
RUN pip install pyaudio
RUN apt-get install -y alsa-utils


CMD ["python3", "run.py"]
