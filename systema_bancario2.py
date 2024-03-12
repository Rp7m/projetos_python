from datetime import datetime
from getpass import getpass

menu = ''''
#################################
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
#################################
'''
menu1 = '''
#################################
Sistema bancario.
Digite a opção desejada
[1] Logar na conta
[2] Cadastrar
[3] Abrir conta bancaria
[4] Encerrar programa
#################################

'''
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3
AG = "0001"
usuario = {}
conta = {}
operacoes = {}

data_hora = datetime.now()
data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
data = data_hora_formatada[:10]
hora = data_hora_formatada[11:]
#indice = 0
ultima_operacao = 0

def func_extrat(operacoes,*,extrato,numero_conta):

     lista = len(extrato)
     if lista == 0:
             print("Não foram realizadas movimentações")          
     else:
        titulo1 = "Data"
        titulo2 = "Horario"
        titulo3 = "Operação"
        print(titulo1.center(12,"-")+titulo2.center(11,"-")+titulo3.center(10,"-"))
             

        for indice,dados in enumerate(extrato):

            d = extrato[indice][0] # Data de deposito
            h = extrato[indice][1] # Hora hora de deposito
            dep = str(extrato[indice][2]) # Deposito
            print(d.center(12)+h.center(11)+dep.center(10))
            

        print("-" * 33)
        print(f"Saldo total: R$ {saldo:.2f}")  
        print("-" * 33)
        return 

def func_depositar(valor,extrato,operacoes,numero_conta,/):
    global saldo
    if  "," in valor:
            print("""
                    O peração não realizada.
                  Utilize ponto (.) em vez de virgula (,)
                  Ex:
                  R$ 23.55 em vez de R$ 23,55

                  """)
    else:
        deposito = float(valor)

        
        if deposito > 0:
                saldo += deposito
                extrato.append([data,hora,f'{deposito:.2f}'])
                operacoes[numero_conta] = {'extrato':extrato,'saldo':f'{saldo:.2f}'}


                print("Operação realizada com sucesso")
               
               
                
        else:
            print("Não foi possivel realizar a operação")
    return saldo
     
def fun_sacar(*,valor,extrato,numero_conta):
    global numero_saques
    global saldo
    global LIMITE_SAQUE
    global limite
    if len(extrato) != 0:
        ultima_operacao = len(extrato) - 1
    if numero_saques == LIMITE_SAQUE and extrato[ultima_operacao][0] == data:
            print("Operação não realizada,limite de saque diário estourado")
    else:
        
        if "," in valor:
            print("""
                    O peração não realizada.
                   Utilize ponto (.) em vez de virgula (,)
                  Ex:
                  R$ 23.55 em vez de R$ 23,5               
                  """)
        else:
            saque = float(valor)
            
            if saque > saldo:
                print("Operação não realizada por falta de saldo")
            elif saque > 0 and saque <= limite:
                saldo -= saque
                extrato.append([data,hora,"-"+str(saque)])
                operacoes[numero_conta] = {'extrato':extrato,'saldo':f'{saldo:.2f}'}

                print("Operação realizada com sucesso")
                
                
                if extrato[ultima_operacao][0] != data:
                             numero_saques = 0
               
                numero_saques += 1
            
                
            else:
                print("O peração não realiza valor maior que o limite diário ou valor invalido.")

def func_limpa_saldo():
     global saldo
     saldo = 0



def func_cadastrar_usuario(cpf,nome,dat_nascimento,endereco,senha):
     global usuario
     usuario[cpf] = {'nome':nome,'dat_nascimento':dat_nascimento,'endereco':endereco,'senha':senha}
     print("Cadastrado realizado com sucesso")

def func_verificar_cpf(cpf):
     tamanho = len(cpf)
     resposa = ""
     numeros = "1234567890"
     
     if tamanho == 11:
          for cpf in cpf:
            if cpf in numeros:
                 resposta = "valido"
            else:
                 
                 resposta = "invalido"
                 return resposta             
     else:
          resposta = "invalido"
          return resposta
     return resposta


def func_consulta_cpf(usuario,cpf):
     total = len(usuario)
     retorno = False

     if total == 0:
          retorno = False
          return retorno,total
     else:
          for usuario in usuario:
               if cpf != usuario:
                    retorno = False
                    
               else:
                    retorno = True
                    return retorno,total
     return retorno,total

def func_logar(usuario,cpf,senha):
     retorno = False
     for indice,dados in usuario.items():
               if indice == cpf:
                    if dados['senha'] == senha:
                         retorno = True
                         return retorno
                    else:
                         print("Usuario e senha incorreta")
               else:
                   retorno = False
     return retorno

def func_criar_conta(AG,conta,cpf):
     total = len(conta)
     total += 1
     conta[total]={'agencia':AG,'usuario':cpf}
     print(f"Parabéns {usuario[cpf]['nome']} conta aberta com sucesso")
     print(f"Agencia: {conta[total]['agencia']} conta: {total}")


def func_verifica_conta(conta,agencia,numero_conta,cpf):
     retorno = False
     if len(conta) >= numero_conta and numero_conta != 0:
      if conta[numero_conta].get('usuario') == cpf and conta[numero_conta].get('agencia') == agencia:
           retorno = True
 
     return retorno




def func_menu_operacao(usuario,cpf,numero_conta):
      while True:
                    print(f""" 
                          
Benvindo {usuario[cpf]['nome']} """)

                    opcao = input(menu)

                    if opcao == "d":

                        valor = input("Digite o valor de deposito: ")
  
                        retorno_saldo = func_depositar(valor,extrato,operacoes,numero_conta)
                        print(f"saldo total: {saldo}")
  
  
                    elif opcao == "s":
                       valor = input("Digite o valo do saque R$:")
                       fun_sacar(valor=valor,extrato=extrato,numero_conta=numero_conta)


                    elif opcao == "e":
                        func_extrat(operacoes,extrato=extrato,numero_conta=numero_conta)


                    elif opcao == "q":
                       func_limpa_saldo()
                       extrato.clear()
                       break
                       
                    else:
                        print("Operação inválida,por favor selecione novamente a operação desejada.")        
            
      
def func_main():

     while True:
    
          opicao_inicial = input(menu1)

          if opicao_inicial == "1":
          
                print("########## Login ##########")

                cpf = input("Digite seu cpf: ")
                agencia = input("Digite a sua agência :")
                numero_conta = int(input("Digite o numero da sua conta: "))
                senha = getpass("Digite sua senha: ")


                if func_logar(usuario,cpf,senha) == True and func_verifica_conta(conta,agencia,numero_conta,cpf) == True:
                     func_menu_operacao(usuario,cpf,numero_conta)

                else:
                     print("Usuario e senha incorreto")


          elif opicao_inicial == "2":
               print("##########Cadastro##########")
               cpf = input("Digite seu CPF: ")
               verifica = func_verificar_cpf(cpf)

               if verifica == "valido":
                    retorno,total = func_consulta_cpf(usuario,cpf)

                    if retorno == False or retorno == False and total == 0:
                          nome = input("Digite seu nome: ")
                          dat_nascimento = input("Data de nascimento: ")
                          endereco = input("""Digite seu endereço no formato:
                                           logradouro,nro - bairro - cidade/sigla estado
                                           """)
                          senha = getpass("Digite a senha ")

                          func_cadastrar_usuario(cpf,nome,dat_nascimento,endereco,senha)
                    else:
                         print("O usuario já existe")       
               else:
                  print("O formato do CPF está invalido, digite somente numeros")

          elif opicao_inicial == "3":
               print("#######< Criar conta >#########")
               cpf = input("Digite seu CPF: ")
               retorno,total = func_consulta_cpf(usuario,cpf)

               if retorno == True:
                    senha = getpass("Digite sua Senha :")
                    if func_logar(usuario,cpf,senha):
                         func_criar_conta(AG,conta,cpf)
                    else:
                         print("Usuário e senha incorreta ")

               else:
                    print("Usuário não encontrado,para abrir uma conta é preciso ter cadastro")




          elif opicao_inicial == "4":
              break
          else:
               print("Operação inválida,por favor selecione novamente a operação desejada.")


        
    
     



func_main()