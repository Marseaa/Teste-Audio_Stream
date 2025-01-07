import asyncio
import websockets
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 5

async def send_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Gravando áudio...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Áudio gravado. Enviando para o servidor...")
    async with websockets.connect("ws://localhost:8000") as websocket:
        await websocket.send(b"".join(frames))
        print("Áudio enviado. Aguardando transcrição...")
        response = await websocket.recv()
        print("Transcrição recebida:", response)

asyncio.run(send_audio())
