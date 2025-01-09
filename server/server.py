from faster_whisper import WhisperModel
import asyncio
import websockets
import wave

# Inicializar o modelo Faster Whisper
whisper_model = WhisperModel("large-v3", device="cuda", compute_type="float16")

def get_Transcription(datablock, audio_path):
    # Fazer a transcrição automática usando Faster Whisper
    segments, info = whisper_model.transcribe(audio_path, beam_size=5, language="pt")
    transcription = " ".join(segment.text for segment in segments)
    return transcription

async def process_audio(websocket):
    async for message in websocket:
        with open("received.wav", "wb") as f:
            f.write(message)

        print("Áudio recebido. Transcrevendo...")
        transcription = get_Transcription(None, "received.wav")
        await websocket.send(transcription)
        print("Transcrição enviada:", transcription)

async def main():
    async with websockets.serve(process_audio, "localhost", 8000):
        print("Servidor WebSocket rodando em ws://localhost:8000")
        await asyncio.Future()  # Mantém o servidor rodando

asyncio.run(main())
