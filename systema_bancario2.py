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
Bem vindo ao sistema bancario.
Digite a opção desejada
[1] Logar
[2] Cadastrar
[3] Sair
#################################

'''
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3
usuario = {}

data_hora = datetime.now()
data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
data = data_hora_formatada[:10]
hora = data_hora_formatada[11:]
#indice = 0
ultima_operacao = 0

def func_extrat(extrato):
    #global extrato
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
        return extrato

def func_depositar(entrada,extrato):
    global saldo
    if  "," in entrada:
            print("""
                    O peração não realizada.
                  Utilize ponto (.) em vez de virgula (,)
                  Ex:
                  R$ 23.55 em vez de R$ 23,55

                  """)
    else:
        deposito = float(entrada)

        
        if deposito > 0:
                saldo += deposito
                extrato.append([data,hora,f'{deposito:.2f}'])
                print("Operação realizada com sucesso")
               
                
        else:
            print("Não foi possivel realizar a operação")
    return extrato
     
def fun_sacar(entrada,extrato=extrato):
    global numero_saques
    global saldo
    global LIMITE_SAQUE
    global limite
    if len(extrato) != 0:
        ultima_operacao = len(extrato) - 1
    if numero_saques == LIMITE_SAQUE and extrato[ultima_operacao][0] == data:
            print("Operação não realizada,limite de saque diário estourado")
    else:
        
        if "," in entrada:
            print("""
                    O peração não realizada.
                   Utilize ponto (.) em vez de virgula (,)
                  Ex:
                  R$ 23.55 em vez de R$ 23,5               
                  """)
        else:
            saque = float(entrada)
            
            if saque > saldo:
                print("Operação não realizada por falta de saldo")
            elif saque > 0 and saque <= limite:
                saldo -= saque
                extrato.append([data,hora,"-"+str(saque)])
                print("Operação realizada com sucesso")
                
                if extrato[ultima_operacao][0] != data:
                             numero_saques = 0
               
                numero_saques += 1
            
                
            else:
                print("O peração não realiza valor maior que o limite diário ou valor invalido.")
        
def func_cadastrar_usuario(cpf,nome,dat_nascimento,endereco,senha):
     global usuario
     usuario[cpf] = {'nome':nome,'dat_nascimento':dat_nascimento,'endereco':endereco,'senha':senha}
     print(usuario)
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
     retorno = ""

     if total == 0:
          retorno = "cadastrar"
          return retorno
     else:
          for usuario in usuario:
               if cpf != usuario:
                    retorno = "cadastrar"
                    
               else:
                    retorno = "nao cadastrar"
                    return retorno
     return retorno

def func_logar(cpf,senha1):
     global usuario
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
    
    
            
    



while True:
    
    opicao_inicial = input(menu1)

    if opicao_inicial == "1":

          print("########## Login ##########")

          cpf = input("Digite seu cpf: ")
          senha = getpass("Digite sua senha: ")
          
          if func_logar(cpf,senha) == True:
               while True:
                    
                    opcao = input(menu)

                    if opcao == "d":

                        entrada = input("Digite o valor de deposito: ")
  
                        func_depositar(entrada,extrato)
  
  
                    elif opcao == "s":
                       entrada = input("Digite o valo do saque R$:")
                       fun_sacar(entrada,extrato=extrato)


                    elif opcao == "e":
                        func_extrat(extrato)


                    elif opcao == "q":
                       break
                    else:
                        print("Operação inválida,por favor selecione novamente a operação desejada.")
          else:
               print("Usuario e senha incorreto")



        
    
    elif opicao_inicial == "2":
         print("##########Cadastro##########")
         cpf = input("Digite seu CPF: ")
         verifica = func_verificar_cpf(cpf)
         
         if verifica == "valido":
              #print("valido")
              if func_consulta_cpf(usuario,cpf) == "cadastrar":
                    nome = input("Digite seu nome: ")
                    dat_nascimento = input("Data de nascimento: ")
                    endereco = input("""Digite seu endereço no formato:
                                     logradouro,nro - bairro - cidade/sigla estado
                                     """)
                    senha = getpass("Digite a senha ")
                    print(senha)
                    func_cadastrar_usuario(cpf,nome,dat_nascimento,endereco,senha)
              else:
                   print("O usuario já existe")       
         else:
            print("O formato do CPF está invalido, digite somente numeros")
       

         

         
    elif opicao_inicial == "3":
        break
    else:
         print("Operação inválida,por favor selecione novamente a operação desejada.")


        
    
   