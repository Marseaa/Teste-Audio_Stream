import torch
from transformers import pipeline

print("===== Teste do PyTorch =====")
print("CUDA disponível:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Versão do CUDA detectada pelo PyTorch:", torch.version.cuda)
    print("Versão do cuDNN detectada pelo PyTorch:", torch.backends.cudnn.version())
    print("Número de GPUs disponíveis:", torch.cuda.device_count())
    print("Nome da GPU:", torch.cuda.get_device_name(0))
    
    print("cuDNN está habilitado:", torch.backends.cudnn.is_available())
else:
    print("Erro: CUDA não está disponível no PyTorch.")


print("\n===== Teste do Transformers =====")
try:
  
    nlp_pipeline = pipeline("fill-mask", model="bert-base-uncased", device=0 if torch.cuda.is_available() else -1)
    print("Pipeline de Transformers carregado com sucesso usando a GPU.")
except Exception as e:
    print("Erro ao carregar o pipeline do Transformers:")
    print(e)


def transcrever_audio(audio_path):
    asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=0 if torch.cuda.is_available() else -1)
    print(f"Processando o arquivo de áudio: {audio_path}")
    result = asr_pipeline(audio_path)
    return result.get("text", "Transcrição não disponível.")

def main():
    audio_path = "temp_audio.wav"
    print("Lendo o arquivo de áudio:", audio_path)
    transcription = transcrever_audio(audio_path)
    print("Resultado da transcrição:", transcription)

if __name__ == "__main__":
    main()