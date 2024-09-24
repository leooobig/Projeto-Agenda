from ddd import ddds
from classes import Agenda,Contato
import os
import json

def mostrarMenu():
    print(f'1. Adicionar Contato\n2. Remover Contato\n3. Editar Contato\n4. Buscar Contato\n5. Exibir todos os Contatos\n6. Sair')

def validarOpcao():
    while True:
        opcao = input('Digite uma opção do menu: ')
        if opcao in ['1','2','3','4','5','6']:
            return opcao
        else:
            print('Opção inválida, tente novamente.')
            continue

def validarNumero(): #Função válidando se o que o cliente digitou é um número e tem 9 digitos.
    while True:
        numero = input('Digite um número para o cadastro: ')
        numero_existe = False

        for i in agenda.contatos:
            if numero == i['numero']:
                numero_existe = True
        if numero_existe:
            print('O número ja existe na lista de contatos, por favor tente outro')
            continue
        if numero.isdigit() and len(numero) == 9:
            return numero
        else:
            print('O número não pode conter letras e tem que conter 9 digitos.')
            continue

def validarNome():
    while True:    
        nome =  input('Digite o nome do contado: ')
        if not any(char.isdigit() for char in nome): #Verifica se todos os caracteres que o usuário digitou é uma letra
            if len(nome) != 0:
                return nome
            else:
                print('O nome não pode ser vazio')
                continue
        else:
            print('O nome não pode conter números')
            continue

def validarDDD(lista):
    while True:
        ddd = input('Digite o DDD do número: ')
        try:
            ddd = int(ddd)
            for i, j in lista.items(): #Verifica se o DDD que o usuário digitou está dentro da lista de DDD
                if ddd in j:
                    return i
        except ValueError:
            print('O DDD só pode conter números.')
            continue
        print('DDD não existe no Brasil.')
        continue

def validarEmail():
    while True:
        email = input('Digite o email do contato: ')
        email_existe = False

        for i in agenda.contatos:
            if email == i['email']:
                email_existe = True
        if email_existe:
            print('Email ja cadastrado em outro número, tente outro.')
            continue
        if "@" in email and "." in email[email.index("@"):]: #Verifica se existe "@" dentro da string e um "." depois do "@"
            return email
        print('Email inválido, por favor digite novamente')
        continue

def validarEdicao():
    loopEdicao = True
    while loopEdicao:
            editar_contato = input('Digite o número do contato que deseja editar: ')
            for i in agenda.contatos:
                if editar_contato == i['numero']: #Verifica se o número que o usuário digitou para edição existe na Agenda
                    print(f'Você está editando: - Nome: {i['nome']} | Número: {i['numero']} | Estado: {i['estado']} | Email: {i['email']}')
                    escolha = input('Escolha o que deseja editar (Nome) (Número) (Estado) (Email) ').lower()

                    if escolha == 'nome':
                        novo_nome = validarNome()
                        i['nome'] = novo_nome
                        loopEdicao = False
                    elif escolha == 'número':
                        novo_numero = validarNumero()
                        i['numero'] = novo_numero
                        loopEdicao = False
                    elif escolha == 'estado':
                        novo_DDD = validarDDD(ddds)
                        i['estado'] = novo_DDD
                        loopEdicao = False
                    elif escolha == 'email':
                        novo_email = validarEmail()
                        i['email'] = novo_email
                        loopEdicao = False
                    else:
                        print('Escolha uma opção válida para editar')

def criandoContato(): #Junta as funções de cima e valida em uma só. E ainda cria um novo objeto de Contato para cada vez chamada tal função
    numero = validarNumero()
    nome = validarNome()
    estado = validarDDD(ddds)
    email = validarEmail()
    contato = Contato(numero,nome,estado,email)
    contato = contato.completarCadastro()
    os.system('cls')
    print(f'{nome}, com o número {numero}, do estado de {estado} e do email {email} adicionado a agenda.')
    print()
    return contato

agenda = Agenda()
validandoPrograma = True
while validandoPrograma:
    mostrarMenu()
    print()
    opcao = validarOpcao()

    if opcao == '1':
        os.system('cls')
        contato = criandoContato()
        agenda.adicionarContato(contato)
    
    if opcao == '2':
        os.system('cls')
        if len(agenda.contatos) == 0:
            print('Não existem contatos na agenda para remover')
            continue
        agenda.listarAgenda()
        deletarnum = input('Digite um número para ser deletado: ')
        agenda.deletarContato(deletarnum)
    
    if opcao == '3':
        os.system('cls')
        if len(agenda.contatos) == 0:
            print('Não existem contatos na agenda para editar')
            continue
        agenda.listarAgenda()
        validarEdicao()
        os.system('cls')
    
    if opcao == '4':
        os.system('cls')
        if len(agenda.contatos) == 0:
            print('Não existem contatos na agenda para buscar')
            continue
        buscaAgenda = input('Digite um nome para buscar na agenda: ')
        print()
        print(f'Todos os contatos com o filtro de busca: "{buscaAgenda}"')
        for i in agenda.contatos:
            if buscaAgenda.lower() in i['nome'].lower() or i['nome'].lower() in buscaAgenda.lower():
                print(f'Nome: {i['nome']} | Número: {i['numero']} | Estado: {i['estado']} | Email: {i['email']}')
        print()

    if opcao == '5':
        os.system('cls')
        if len(agenda.contatos) == 0:
            print('NNão existem contatos na agenda para listar.')
        agenda.listarAgenda()
    
    if opcao == '6':
        os.system('cls')
        exit()