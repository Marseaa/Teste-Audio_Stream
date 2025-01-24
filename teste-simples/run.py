
import pyaudio
import wave
import torch
from transformers import pipeline

def capturar_audio(nome_arquivo, taxa_amostragem=16000, duracao=10, canais=1):
    formato = pyaudio.paInt16
    pa = pyaudio.PyAudio()

    stream = pa.open(format=formato,
                     channels=canais,
                     rate=taxa_amostragem,
                     input=True,
                     frames_per_buffer=1024)

    print("Pressione ENTER para começar a gravar...")
    input()
    print("Gravando... Pressione ENTER novamente para parar.")
    frames = []

    try:
        while True:
            data = stream.read(1024, exception_on_overflow=False)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    print("Gravação finalizada.")
    stream.stop_stream()
    stream.close()
    pa.terminate()

    with wave.open(nome_arquivo, 'wb') as wf:
        wf.setnchannels(canais)
        wf.setsampwidth(pa.get_sample_size(formato))
        wf.setframerate(taxa_amostragem)
        wf.writeframes(b''.join(frames))

def transcrever_audio(audio_path):
    asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=0 if torch.cuda.is_available() else -1)
    print(f"Processando o arquivo de áudio: {audio_path}")
    result = asr_pipeline(audio_path)
    return result.get("text", "Transcrição não disponível.")

def main():
    nome_arquivo = "temp_audio.wav"
    capturar_audio(nome_arquivo)
    transcription = transcrever_audio(nome_arquivo)
    print("Resultado da transcrição:", transcription)

if __name__ == "__main__":
    main()

