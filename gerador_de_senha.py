import random
import string

def gerar_senha(tamanho=12, usar_maiusculo=True, usar_minusculo=True, usar_digitos=True, usar_simbolos=True):
    grupos = [
        (usar_maiusculo, string.ascii_uppercase),
        (usar_minusculo, string.ascii_lowercase),
        (usar_digitos, string.digits),
        (usar_simbolos, string.punctuation),
    ]

    caracteres = "".join(conjunto for usar, conjunto in grupos if usar)

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

print("######## Gerador de Senhas ########")

tamanho = int(input("Digite o tamanho desejado da senha: "))
usar_maiusculo = input("Deseja usar letras maiúsculas na senha: (s/n) ").lower() == "s"
usar_minusculo = input("Deseja usar letras minúsculas na senha: (s/n) ").lower() == "s"
usar_digitos = input("Deseja usar números na senha: (s/n) ").lower() == "s"
usar_simbolos = input("Deseja usar símbolos na senha: (s/n) ").lower() == "s"

minha_senha = gerar_senha(tamanho, usar_maiusculo, usar_minusculo, usar_digitos, usar_simbolos)
print(f"Senha gerada: ", minha_senha)