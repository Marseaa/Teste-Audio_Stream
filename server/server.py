from transformers import pipeline
import asyncio
import websockets
import torch

asr_pipeline = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3",
    device=0 if torch.cuda.is_available() else -1
)

def get_transcription(audio_path):
    print(f"Processando o arquivo de áudio: {audio_path}")
    result = asr_pipeline(audio_path)
    return result.get("text", "Transcrição não disponível.")

async def process_audio(websocket):
    async for message in websocket:
        with open("received.wav", "wb") as f:
            f.write(message)

        print("Áudio recebido. Transcrevendo...")
        transcription = get_transcription("received.wav")

        await websocket.send(transcription)
        print("Transcrição enviada:", transcription)

async def main():
    async with websockets.serve(process_audio, "0.0.0.0", 8000):
        print("Servidor WebSocket rodando em ws://0.0.0.0:8000")
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())