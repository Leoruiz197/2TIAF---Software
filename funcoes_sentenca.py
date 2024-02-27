
def identificar_adjuntos_tempo(frase):
    # Palavras que indicam tempo
    palavras_tempo = ["ontem", "hoje", "amanhã", "sempre", "agora", "depois", "cedo", "tarde", "quando",
                      "frequentemente", "momento", "durante", "próxima", "antes", "antigamente"]

    # Stopwords
    stopwords = ["na", "no", "nas", "nos", "da", "do", "das", "dos", "a", "o", "em", "de"]

    adjuntos_completos = ["na próxima"]

    # Remover pontuações e dividir a frase em palavras
    palavras = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in frase).split()

    # Criar combinações de palavras_tempo com stopwords
    combinacoes_tempo_stopwords = [tempo + " " + stopword for tempo in palavras_tempo for stopword in stopwords]

    # Remover stopwords
    palavras_sem_stopwords = [palavra.lower() for palavra in palavras if palavra.lower() not in stopwords]

    # Identificar adjuntos adverbiais de tempo
    adjuntos_tempo = [palavra.lower() for palavra in palavras_sem_stopwords if palavra.lower() in palavras_tempo]

    # Identificar adjuntos completos
    adjuntos_completos.extend([combinacao for combinacao in combinacoes_tempo_stopwords if combinacao.lower() in frase.lower()])

    return adjuntos_tempo, adjuntos_completos

# Exemplo de uso
frase_exemplo = "Na próxima semana, teremos uma reunião. Hoje, estou ocupado."
resultado_tempo, resultado_completo = identificar_adjuntos_tempo(frase_exemplo)

# Exibindo os resultados
print("Frase:", frase_exemplo)
print("Adjuntos Adverbiais de Tempo:", resultado_tempo)
print("Adjuntos Adverbiais Completos:", resultado_completo)
