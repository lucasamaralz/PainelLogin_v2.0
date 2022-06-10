import time
import os
from modulos.PainelInfo import Central_Info
from modulos.PainelUsuario import Central_Usuario

t = 0.5
t1 = 1
t1_5 = 1.5
t3 = 3

print('Bem-Vindo ao Sistema de Login!! \n ')
nvarb=input('Digite seu Nome: ')

nome = nvarb.lstrip().lower().title()

db = 'contas.txt'

os.system("cls")

class Sistema_login():
    def Menu():
        print(f'\nEscolha um dos Itens a Baixo {nome}: \n Login - Cadastro - Info - Ctxt \n')
        Escolha = input('Digite: ')
        Ajuste_Escolha = Escolha.lstrip().lower().rstrip()

        if (Ajuste_Escolha=="login"):
            time.sleep(t)
            Sistema_login.Login()

        if (Ajuste_Escolha=="cadastro"):
            time.sleep(t)
            Sistema_login.Cadastro()


        if (Ajuste_Escolha=="info"):
            time.sleep(t)
            Sistema_login.Info()


        if (Ajuste_Escolha=="ctxt"):
            time.sleep(t)
            Sistema_login.Ctxt()

        else:
            print('Digite Novamente: \n')
            Sistema_login.Menu()
    def Ctxt():
        try:
            print('Digite "Limpar" para eliminar a DATABASE! ')
            limpar = input('Digite: ')
            limparstr = limpar.lstrip().lower().title().rstrip()

            if (limparstr=="Limpar"):
                os.remove('contas.txt')
                print('Limpando o Arquivo...')
                time.sleep(t1_5)
                print('O Arquivo Foi Apagado\n Retornando ao Menu')
                time.sleep(t1_5)
                Sistema_login.Menu()
            else:
                print('Você Digitou Errado \n A DATABASE não foi apagada, Escreva Novamente')
                Sistema_login.Ctxt()

        except:
             print('O Arquivo já foi Apagado!\n Você será redirecionado ao Menu!')
             time.sleep(t1)
             Sistema_login.Menu()
    def Login():
        if os.path.exists('contas.txt')==True:
            contas = open('contas.txt')
            print('Digite seu Usuário ')
            user_cadastro = input('Usuário: ')
            print('Digite sua Senha: ')
            user_senha = input('Senha: ')
            contas = contas.readlines()

            if user_cadastro + '\n' in contas and user_senha + '\n' in contas:
                print('Você está logando!')
                time.sleep(t3)
                print(f'Logado com SUCESSO! {nome}')
                Central_Usuario.Painel()
                exit('Finalizando o Codigo!')

            else:
                print('Sua senha está ERRADA!!\n Você será redirecionado ao MENU!')
                time.sleep(t)
                Sistema_login.Menu()
        else:
             print('Você não possui um Banco de Dados, Acesse o Menu de Cadastro e Crie Um!')
             time.sleep(t1)
             Sistema_login.Menu()
    def Logado():
        print('Redirencionando!')
        Central_Usuario.Painel()
    def Cadastro():
        contas = open('contas.txt', 'w')
        contas.close()
        contas = open('contas.txt' , 'a')
        print('Usuário ')
        user_cadastro = str(input('Digite o Usuário: '))
        contas.write('{}\n'.format(user_cadastro))
        user_senha = str(input('Digite o Senha: '))
        contas.write('{}\n'.format(user_senha))
        print(f'Cadastro Realizado com Sucesso {nome}!!! \n Você será redirecionado para o Menu!!')
        time.sleep(t1)
        contas.close()
        Sistema_login.Menu()
    def Info():
        Central_Info.Info()
        time.sleep(t1)
        Sistema_login.Menu()
Sistema_login.Menu()





