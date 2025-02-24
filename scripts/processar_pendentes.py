import os
from rembg import remove
from PIL import Image

# Definir a pasta base onde estão as imagens
PASTA_BASE = "./imagens"
PASTA_ALVO = "neymarImg"  # Mude este nome para processar outra pasta!

pasta_original = os.path.join(PASTA_BASE, PASTA_ALVO)
pasta_saida = os.path.join(pasta_original, "sem_fundo")
os.makedirs(pasta_saida, exist_ok=True)

# Formatos suportados
formatos_suportados = (".jpg", ".jpeg", ".png")

# Obter lista de arquivos originais e já processados
arquivos_originais = [f for f in os.listdir(pasta_original) if f.lower().endswith(formatos_suportados)]
arquivos_processados = [f for f in os.listdir(pasta_saida) if f.lower().endswith(".png")]

# Criar lista de imagens que ainda precisam ser processadas
pendentes = []
for i, arquivo in enumerate(arquivos_originais, start=1):
    novo_nome = f"Neymar{i:02d}.png"
    if novo_nome not in arquivos_processados:  # Só adiciona se ainda não foi feito
        pendentes.append((arquivo, novo_nome))

# Processar apenas as imagens pendentes
if not pendentes:
    print("✅ Todas as imagens já foram processadas!")
else:
    print(f"🔄 Processando {len(pendentes)} imagens pendentes...")

    for arquivo_original, novo_nome in pendentes:
        caminho_original = os.path.join(pasta_original, arquivo_original)
        caminho_saida = os.path.join(pasta_saida, novo_nome)

        try:
            with Image.open(caminho_original) as img:
                img = img.convert("RGBA")
                img_sem_fundo = remove(img)
                img_sem_fundo.save(caminho_saida, "PNG")
                print(f"✅ Fundo removido: {arquivo_original} ➝ {novo_nome}")

        except Exception as e:
            print(f"❌ Erro ao processar {arquivo_original}: {e}")

    print("🚀 Processamento finalizado!")
