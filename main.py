from colorama import Fore, Back, Style
from getpass import getpass
import json
import wget

#boas vindas
print(Fore.BLACK + "----------------------------------")
print(Fore.BLUE + "Bem vindo a Autoescola do Miguel!")
print(Fore.BLACK + "----------------------------------")
print(Fore.WHITE + "Somos a melhor Autoescola do Brasil!")
print("Para continunar, você precisa fazer um cadastro ou login.")
print("") 

def inicio():  # Função para iniciar o programa
    while True: # Loop principal para cadastro/login
        opcao = int(input(Fore.BLACK + "Você deseja fazer (1) Cadastro, (2) Login ou (3) Sair? Digite 1, 2 ou 3: "))
        if opcao == 1:  # Opção de cadastro
            cadastro()
            idade = login() # Após cadastro, fazer login
            break   
        elif opcao == 2:   # Opção de login
            idade = login()  # Fazer login
            if idade is not None:   # Verificar se login foi bem-sucedido
                break   # Sair do loop se login for bem-
        elif opcao == 3:  # Opção de sair
            sair()
            exit()  # Encerra o programa
        else:
            print(Fore.RED + "Opção inválida! Por favor, digite 1 para Cadastro, 2 para Login ou 3 para Sair.")
            print(Fore.WHITE + "")
def cadastro():  # Função para cadastro do usuário
    nome = input("Qual seu nome? ").strip()  # Solicitar nome do usuário
    senha = getpass("Crie uma senha: ").strip()  # Solicitar senha sem exibir na tela
    novo_usuario ={
        "nome": nome,
        "senha": senha
    }
    try:
        with open("cadastro.json", "r") as arquivo:
            usuarios = json.load(arquivo) # Vai carregar a lista de usuarios existentes
    except FileNotFoundError:
        usuarios = [] # Se o arquivo não existir, criar lista vazia
    
    for usuario in usuarios:
        if usuario["nome"] == nome: # Verifica se o nome q foi digitado, ja existe no arquivo
            print(Fore.RED + "Usuario ja existe, por favor, faça login.")
            print(Fore.WHITE + "")
            return login()
        
    usuarios.append(novo_usuario)   # Usando o append para adicionar um novo cadastro, sem apagar os outros
    with open("cadastro.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print(Fore.GREEN + "Cadastro realizado com sucesso!")
    print(Fore.WHITE + "    ")
    return True



def login():  # Função para login do usuário
    try:
        with open("cadastro.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        nome = input("Informe seu nome para login: ").strip()
        senha = getpass("Informe sua senha: ").strip()
        for usuario in usuarios:
                if nome == usuario["nome"] and senha == usuario["senha"]:
                    print(Fore.BLUE + "Login realizado com sucesso!")
                    print(Fore.WHITE + "")
                    return cpf()  # Ir para validação do cpf após login
        else:
            print(Fore.BLUE + "Usuario não encontrado. Vamos redirecionar você para tela inicial...")
            inicio()
    except FileNotFoundError:  # Tratamento de erro se o arquivo não existir
        print(Fore.RED + "Algo deu errado. Tente novamente")
        print(Fore.WHITE + "")
        return None

def sair():  # Função para sair do programa
    print(Fore.BLACK + "-----------------------------------------------------------")
    print(Fore.BLUE + "Obrigado por acessar a Autoescola do Miguel! Volte sempre!")
    print(Fore.BLACK + "-----------------------------------------------------------")
    print(Fore.WHITE + "")

def cpf():  # Função para validar CPF
    while True: # Loop até o CPF ser válido
        cpf1 = input("Informe seu CPF (somente números): ")
        if len(cpf1) == 11 and cpf1.isdigit():
            print(Fore.GREEN + "CPF válido!")
            print(Fore.WHITE + "")
            return maior_de_idade()  # Chamar função para validar idade
        else:
            escolha2 = input(Fore.RED + "CPF inválido! Deve conter 11 números. (1)Tentar novamente ou (2)Sair?").strip()
            print(Fore.WHITE + "")
            if escolha2 == "2":
                sair()  # Sair do programa
                exit()  # Encerra o programa
            elif escolha2 == "1":
                return cpf()  # Tentar validar CPF novamente
            else:
                print(Fore.RED + "Opção inválida! Voltando para a tela inicial.")
                print(Fore.WHITE + "")
                return inicio()  # Voltar para tela inicial 
                
def maior_de_idade():  # Função para validar idade
        idade = int(input("Qual a sua idade? "))
        if 18 <= idade <= 80:
            print(Fore.GREEN + "Idade válida! Você pode tirar a CNH.")
            print(Fore.WHITE + "")
            return escolha()  # Chamar função para escolher tipo de CNH
        else:
            escolha1 = input(Fore.BLACK + "Idade inválida! Você deve ter mais de 18 e até 80 anos para tirar CNH. (1)Voltar a tela incial ou (2)Sair? ").strip()
            print(Fore.WHITE + "")
            if escolha1 == "1":
                return inicio()  # Voltar para tela inicial
            elif escolha1 == "2":
                sair()  # Sair do programa
                exit()  # Encerra o programa
            else:
                print(Fore.RED + "Opção inválida! Vamos redirecionar você para a tela inicial.")
                print(Fore.WHITE + "")
                return inicio()  # Voltar para tela inicial

def escolha():  # Função para escolher tipo de CNH
    while True:
        escolha = input("Você deseja tirar carta de moto ou de carro? ").lower()
        if escolha == "moto":
            print("Ok, vamos tirar a CNH para MOTO!")
            return tirando_cnh()  # Chamar função para teste teórico
        elif escolha == "carro":
            print("Ok, vamos tirar a CNH para CARRO!")
            return tirando_cnh()  # Chamar função para teste teórico
        else:
            print(Fore.RED + "Você deve escolhar entre MOTO ou CARRO!")
            print(Fore.WHITE + "")

def tirando_cnh():  # Função para teste teórico
    print(Fore.BLUE + "Você está tirando a CNH!")
    print(Fore.BLACK + "Vamos para um teste teórico, com 3 perguntas, responda somente a alternativa correta com (a, b ou c).")
    while True: #Repetição para o teste teórico
        pergunta1 = input(Fore.WHITE + "Qual a cor do semáforo que indica “pare”: A) Verde B) Amarelo C) Vermelho: ").lower().strip()
        pergunta2 = input("Qual a velocidade máxima permitida em uma via urbana: A) 50 km/h B) 80 km/h C) 100 km/h: ").lower().strip()
        pergunta3 = input("O que significa uma linha amarela contínua no centro da via: A) Proibido ultrapassar B) Permitido ultrapassar C) Faixa de pedestres: ").lower().strip()
        if pergunta1 in ["a", "b", "c"] and pergunta2 in ["a", "b", "c"] and pergunta3 in ["a", "b", "c"]:
            if pergunta1 == "c" and pergunta2 == "a" and pergunta3 == "a":
                print(Fore.BLACK + "----------------------------------------------------------------------")
                print(Fore.GREEN + "Parabéns! Você passou no teste teórico! E vai receber seu certificado.")
                print(Fore.BLACK + "----------------------------------------------------------------------")
                print(Fore.YELLOW + "Baixando certificado...")
                print(Fore.WHITE + "")
                link = "https://quatrorodas.abril.com.br/wp-content/uploads/2025/12/Curso-de-instrutor-de-transito-1.jpg?quality=70&strip=info&w=1280&h=720&crop=1"
                wget.download(link, "certificado.jpg",)
                
            else:
                print(Fore.RED + "Infelizmente você não passou no teste teórico. Tente novamente.")
                print(Fore.WHITE + "")
            return pergunta1, pergunta2, pergunta3
        else:
            print(Fore.RED + "Resposta inválida! Por favor, responda com 'a', 'b' ou 'c'.")
            print(Fore.WHITE + "")      


#puxando as funções
inicio ()