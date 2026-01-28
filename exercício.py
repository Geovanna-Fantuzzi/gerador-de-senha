import random #Biblioteca que gera a aleatoriedade
import string #Biblioteca que fornece um conjunto de caracteres para o gerador

def gerar_senha(tamanho=12, usar_maiusculo=True, usar_minusculo=True, usar_digitos=True, usar_simbolos=True):
    grupos = [ #Lista de Tuplas
        # (condição, valor/conteúdo) as tuplas utilizam posições de índice: 0,1
        (usar_maiusculo, string.ascii_uppercase),
        (usar_minusculo, string.ascii_lowercase),
        (usar_digitos, string.digits),
        (usar_simbolos, string.punctuation),
    ]
    # join: Concatena algo
    # join(valor_a_ser_concatenado for tupla[0], tupla[1] in lista_de_tuplas if tupla[0] = True)
    caracteres = "".join(conjunto for usar, conjunto in grupos if usar)

    if not caracteres: # Se a string estiver vazia:
        # Interrompe a execução da função e informa o erro que foi causado por valor inválido
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    
    # random.choice(caracteres): Escolhe um dos caracteres dentro da variável
    # for _ in range(tamanho): Repete a primeira ação de acordo com o valor na variavel 'tamanho'
    # '_' é um elemento ignorado no 'for', o importante aqui são as repetições
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha # Retorna a senha gerada

