import asyncio
import websockets
import whisper
import wave

model = whisper.load_model("base")

async def process_audio(websocket):
    async for message in websocket:
        with open("received.wav", "wb") as f:
            f.write(message)
        
        print("Áudio recebido. Transcrevendo...")
        result = model.transcribe("received.wav")
        await websocket.send(result["text"])
        print("Transcrição enviada:", result["text"])

async def main():
    async with websockets.serve(process_audio, "localhost", 8000):
        print("Servidor WebSocket rodando em ws://localhost:8000")
        await asyncio.Future()  

asyncio.run(main())
