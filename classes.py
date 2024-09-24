import os
class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionarContato(self,contato):
        self.contatos.append(contato)
    
    def deletarContato(self,contato):
            for i in self.contatos:
                if contato == i['numero']:
                    self.contatos.remove(i)
                    os.system('cls')
                    return print(f'Contato (Nome: {i['nome']} | Número: {i['numero']} | Estado: {i['estado']} | Email: {i['email']}) deletado da agenda.')
            os.system('cls')
            print('O que você digitou não condiz com nenhum número da Agenda')
            print()

    def listarAgenda(self):
        for num, i in enumerate(self.contatos):
            print (f'{num+1}. Nome: {i['nome']} | Número: {i['numero']} | Estado: {i['estado']} | Email: {i['email']}')
        print()

class Contato:
    def __init__(self, numero, nome, estado, email):
        self.numero = numero
        self.nome = nome
        self.estado = estado
        self.email = email
        self.contato = {}

    def completarCadastro(self):
        self.contato = {'numero': self.numero,
                        'nome': self.nome,
                        'estado': self.estado,
                        'email': self.email}
        return self.contato
