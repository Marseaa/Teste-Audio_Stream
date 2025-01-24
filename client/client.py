import asyncio
import websockets

async def send_audio_to_server(audio_path="audio_teste.wav"):
    for _ in range(10):  
        try:
            async with websockets.connect("ws://server:8000") as websocket:
                with open(audio_path, "rb") as f:
                    audio_data = f.read()

                print("Enviando áudio para o servidor...")
                await websocket.send(audio_data)

                transcription = await websocket.recv()
                print("Transcrição recebida do servidor:", transcription)
            return
        except ConnectionRefusedError:
            print("Servidor não está pronto. Tentando novamente em 1 segundo...")
            await asyncio.sleep(1)
    print("Falha ao conectar ao servidor.")

async def main():
    await send_audio_to_server()

asyncio.run(main())
