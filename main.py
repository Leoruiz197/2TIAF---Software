from funcoes_processamento import dividir_texto_em_palavras
from funcoes_sentenca import identificar_adjuntos_tempo

titulo = """
  _   _      _        _____
 | \ | |    | |      |  __ \ 
 |  \| |    | |      |  __) | 
 | . ` |    | |      |  ___/  
 | |\  |    | |____  | |       
 |_| \_|    |______| |_|       
                                                                                      
"""

print(titulo)

while True:
    # Exibir o menu
    print("\nMENU:")
    print("1. Dividir texto em um array")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Opção 4")
    print("5. Opção 5")
    print("0. Sair")

    # Solicitar que o usuário escolha uma opção
    escolha = input("Escolha uma opção: ")

    # Verificar a opção escolhida
    if escolha == "1":
        texto = input("digite o texto: ")
        array_palavras = dividir_texto_em_palavras(texto)
        print(array_palavras)
    elif escolha == "2":
        texto =  "Há muito tempo, não o vejo."
        resultado = identificar_adjuntos_tempo(texto)
        print("Adjuntos Adverbiais de Tempo:", resultado)

    elif escolha == "3":
        print("Você escolheu a Opção 3.")
    elif escolha == "4":
        print("Você escolheu a Opção 4.")
    elif escolha == "5":
        print("Você escolheu a Opção 5.")
    elif escolha == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
