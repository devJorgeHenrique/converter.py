import os
import requests

# SUA CHAVE DE API DA REMOVE.BG
API_KEY = "FRBiwkeKuESCC3v1TT8MPUr3"

# Definir a pasta base onde estão as imagens
PASTA_BASE = "./imagens"
PASTA_ALVO = "neymarImg"  # Mude este nome para processar outra pasta!

pasta = os.path.join(PASTA_BASE, PASTA_ALVO)
pasta_saida = os.path.join(pasta, "sem_fundo")
os.makedirs(pasta_saida, exist_ok=True)

# Formatos suportados
formatos_suportados = (".jpg", ".jpeg", ".png")

# Lista de arquivos na pasta
arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(formatos_suportados)]

# Remover fundo de cada imagem
for i, arquivo in enumerate(arquivos, start=1):
    caminho_arquivo = os.path.join(pasta, arquivo)
    novo_nome = f"Neymar{i:02d}.png"  # Ajuste o nome se mudar o tema!
    caminho_saida = os.path.join(pasta_saida, novo_nome)

    print(f"🔄 Removendo fundo: {arquivo} ➝ {novo_nome}")

    # Fazendo a requisição para remover o fundo
    with open(caminho_arquivo, "rb") as img_file:
        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            files={"image_file": img_file},
            data={"size": "auto"},
            headers={"X-Api-Key": API_KEY},
        )

    if response.status_code == 200:
        with open(caminho_saida, "wb") as out_file:
            out_file.write(response.content)
        print(f"✅ Fundo removido: {arquivo} ➝ {novo_nome}")
    else:
        print(f"❌ Erro ao processar {arquivo}: {response.text}")

print("🚀 Remoção de fundo concluída!")
