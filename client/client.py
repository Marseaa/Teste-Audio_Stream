import asyncio
import websockets
import wave
import torchaudio
import io

CHUNK = 1024
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 30  

async def send_audio():
    print("Pressione ENTER para iniciar a gravação.")
    input()  
    print("Gravando áudio por 30 segundos...")
    

    with wave.open("temp_audio.wav", "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  
        wf.setframerate(RATE)

        def callback(indata, frames_per_buffer, time, status):
            if status:
                print("Status:", status)
            wf.writeframes(indata.copy())

        with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype="int16", callback=callback):
            sd.sleep(int(RECORD_SECONDS * 1000))

    print("Áudio gravado. Enviando para o servidor...")


    waveform, sample_rate = torchaudio.load("temp_audio.wav")


    audio_bytes = io.BytesIO()
    torchaudio.save(audio_bytes, waveform, sample_rate, format="wav")
    audio_bytes.seek(0)

    async with websockets.connect("ws://server:8000") as websocket:  
        await websocket.send(audio_bytes.read())
        print("Áudio enviado. Aguardando transcrição...")
        response = await websocket.recv()
        print("Transcrição recebida:", response)

asyncio.run(send_audio())
