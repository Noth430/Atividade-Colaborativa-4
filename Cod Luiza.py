import os
os.system("cls || clear")
from dataclasses import dataclass

"""

Membros da equipe:
- Maria Luiza
- Henrique Santos

"""
""""
    Foi feita uma pesquisa esntre os habitantes de uma região. Foram coletados os dados de idade,sexo(M\F) e salário.
    faça um algoritmo que informe:

a) a média de salário idade do grupo;
b)maior e menor idade do grupo;
c)quantidade de mulheres com salário a partir de R$5.000.00

Crie um menu com três opções.

Código  | Descrição 
        | Adigiconar pessoa
        | Exibir resultados
        | Sair

O final da leitura de dados se dará com quando o usuário digitar o número código 3.
ao adicionar uma família,deve-se limpar o terminal e apresentar o menu novamente.

    - Salve os dados em um arquivo com nome; pesquisa_habitantes.txt.
    - O progama deve ler o arquivo para exibir os dados salvos.

 """


@dataclass
class Habitante:
    idade: int
    genero: str
    salario: float

@dataclass
class Final:
    lista_final: list

def menu():
    print("""
    === MENU ===

1. Adicionar mais uma pessoa/família 
2. Exibir os resultados
3. Sair   
          """)

def sexo(dados):
    
    homens = []
    mulheres = []
    sexo = input("Escolha a opção relacionada a seu sexo: ")

    match sexo:
        case 'Homem':
             homens.append(dados)
        case 'Mulher':
            mulheres.append(dados)
    return dados
    
    
lista_total = []
def criando_arquivo(a,b):
    with open(a, "a") as lista_habitantes:
        for habitante in b:
            lista_habitantes.write(f" {habitante.idade}, {habitante.genero} {habitante.salario},  \n")
        lista_habitantes.close()

def criando_arquivo_final(a,b):
    with open(a, "w") as lista_habitantes:
        for habitante in b:
            lista_habitantes.write(f"{habitante}, \n")
        lista_habitantes.close()

def lendo_arquivo(a):
    with open(a, "r") as arquivos_habitantes:
        for linha in arquivos_habitantes:
            idade, genero, salario = linha.strip().split(",")
            lista_total.append(Habitante(idade=int(idade), genero=str(genero),salario=float(salario)))
            arquivos_habitantes.close()

    return lista_total
    
def media(a):
    QNT = len(a)
    soma = sum(a)

    if QNT == 0:
        return 0
    else:
        media == soma/ QNT
        return media

def limpar_tela():
    os.system("cls || clear")

while True:
    menu()
    opcao = (input("Resposta: "))
    match opcao:
        case "1": 
            habitante = Habitante(
            idade = int(input("Digite a sua idade: ")),
            genero = input("Digite o seu gênero: "),
            salario = float("Digite o valor do seu salário: "))
            lista_total.append(Habitante)
            nome_arquivo_habitante = "pesquisa_habitantes.txt"
            criando_arquivo(nome_arquivo_habitante, lista_total)
            limpar_tela()
        case "2":
            limpar_tela()
            contador = 0
            nome_arquivo_habitante = "dados.txt"
            lista_idade = []
            lista_genero = []
            lista_salario = []
            lista_total_definitiva = lendo_arquivo(nome_arquivo_habitante)
            
            


