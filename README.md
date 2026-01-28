# Gerador de Senhas

Projeto desenvolvido para fins de estudo em Python.

## Bibliotecas Utilizadas
* **random**: Biblioteca que gera a aleatoriedade.
* **string**: Biblioteca que fornece um conjunto de caracteres para o gerador.

---

## Estrutura da Função `gerar_senha`

### Grupos de Caracteres
* **Lista de Tuplas**: Os grupos de caracteres são armazenados em tuplas dentro de uma lista.
* **Tuplas**: Cada tupla armazena a `condição` e o `conteúdo` do grupo. As tuplas utilizam posições de índice para `(condição = 0, conteúdo = 1)`.
* **Conjuntos incluídos**: 
    - `string.ascii_uppercase` (Maiúsculas)
    - `string.ascii_lowercase` (Minúsculas)
    - `string.digits` (Dígitos)
    - `string.punctuation` (Símbolos)

### Processamento e Concatenação
* **join**: Utilizado para concatenar os conjuntos selecionados.
* **Lógica**: `join(valor_a_ser_concatenado for tupla[0], tupla[1] in lista_de_tuplas if tupla[0] == True)`.
* **Tratamento de Erro**: Se a `string` estiver vazia, interrompe a execução da função e informa o erro que foi causado por valor inválido através de um `raise ValueError`.

### Lógica de Geração
* **random.choice(caracteres)**: Escolhe um dos caracteres dentro da string.
* **Repetição**: Ocorre de acordo com o valor na variável `tamanho`.
* **O caractere `_`**: Definido como um elemento ignorado no `for`, onde o importante são apenas as repetições.
* **Retorno**: A função retorna a senha final gerada.

---

## Interação com o Usuário

O script solicita entradas do usuário utilizando os seguintes critérios:
* **.lower()**: Método utilizado para transformar o texto de entrada em minúsculo.
* **== "s"**: Condição que determina o valor aceito como `True` no input para inclusão de caracteres.
