FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive PIP_PREFER_BINARY=1 \
    CUDA_HOME=/usr/local/cuda-11.8 TORCH_CUDA_ARCH_LIST="8.6"

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y wget python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir --upgrade pip && \
    ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#COPY client.py ./

RUN pip install websockets 
RUN pip install sounddevice
RUN pip install torch 
RUN pip install numpy 
RUN pip install ffmpeg-python
RUN pip install torchaudio
RUN pip install --force-reinstall "faster-whisper @ https://github.com/SYSTRAN/faster-whisper/archive/refs/heads/master.tar.gz"

ENTRYPOINT ["python3", "client.py"]
