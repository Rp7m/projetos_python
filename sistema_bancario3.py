from datetime import datetime
from getpass import getpass
from abc import ABC, abstractproperty,abstractclassmethod




class Conta:
     data_hora = datetime.now()
     data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
     data = data_hora_formatada[:10]

     def __init__(self,numero,cliente):
          self._saldo = 0
          self._numero = numero
          self._agencia = "0001"
          self._cliente = cliente
          self._historico = Historico()
          self._quantidade_saques = 0
          


     @property
     def cliente_obj(self):
          return self._cliente
     
     @property
     def historico(self):
          return self._historico

     @property
     def saldo(self):
          return self._saldo
     
     @property
     def numero(self):
          return self._numero
     
     @property
     def agencia(self):
          return self._agencia


     @classmethod
     def nova_conta(cls,cliente,numero):
          return cls(numero,cliente)
     
     def sacar(self,valor,limite):
          saldo = self._saldo
          extrato = self._historico.transacoes
          ultima_operacao = extrato[len(extrato) -1][0] 

          if self._quantidade_saques == limite and ultima_operacao != data:
               self._quantidade_saques = 0


          if self._quantidade_saques == limite:
               print("Saques diários estourados operação não realizada")
             
          else:
               
               if valor > 0:
                    self._saldo -= valor
                    print("Operação realizada com sucesso")
                    self._quantidade_saques += 1
                    return True   
               else:
                    print("valor inválido")
                    return False
               
          
     def depositar(self,valor):
          if valor >0:
               self._saldo += valor
               print("Operação realizada com sucesso")
               return True

          else:
               print("Valor invalido")
               return False
          

class ContaCorrente(Conta):
     def __init__(self, numero, cliente,limite=500,limite_saques=3):
          super().__init__(numero, cliente)
          self._limite = limite
          self._limite_saques = limite_saques
          


     def sacar(self,valor):
          
          limite = self._limite_saques
          
          if valor <= self._limite:
                              if valor > self._saldo:
                                   print("Você não possui saldo para realizar a operação")
                              else:
                                   return super().sacar(valor,limite)
                       
          else:
               print("O valor exede o limite de saque diários")

          return False
               

               

     

class Cliente:
     def __init__(self,endereco,senha):
          self._endereco = endereco
          self._senha = senha
          self._contas = []
     
     def realizar_transacao(self,conta,transacao):
          transacao.registrar(conta)
          
         


     
     def adicionar_conta(self,conta):
          self._contas.append(conta)

     @property
     def senha(self):
          return self._senha
     @property
     def numero_contas(self):
          return self._contas


class PessoaFisica(Cliente):
     def __init__(self,nome,data_nascimento,cpf, endereco,senha):
          super().__init__(endereco,senha)
          self._nome = nome
          self._data_nascimento = data_nascimento
          self._cpf = cpf


     @property
     def cpf(self):
          return self._cpf
     
     @property
     def nome(self):
          return self._nome
        

class Historico:
     data_hora = datetime.now()
     data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
     data = data_hora_formatada[:10]
     hora = data_hora_formatada[11:]

     def __init__(self):
          self._transacoes = []
     
     @property
     def transacoes(self):
          return self._transacoes
     
     def adicionar_transacao_deposito(self,transacao):
          self._transacoes.append(
               
                    [data,hora,f'{transacao.valor:.2f}']
               

          )
     def adicionar_transacao_saque(self,transacao):
          self._transacoes.append(
               
                    [data,hora,f'- {transacao.valor:.2f}']
               

          )
          
          

class Transacao(ABC):
     @property
     @abstractproperty
     def valor(self):
          pass
     @abstractclassmethod
     def registrar(self,conta):
          pass

class Saque(Transacao):
     def __init__(self,valor):
          self._valor = valor

     @property
     def valor(self):
          return self._valor
     
     def registrar(self,conta):
          operacao = conta.sacar(self.valor)

          if operacao:
               conta.historico.adicionar_transacao_saque(self)
               return True
               
          

class Deposito(Transacao):
     def __init__(self,valor):
          self._valor = valor

     @property
     def valor(self):
          return self._valor
     
     def registrar(self,conta):
          transacao = conta.depositar(self.valor)

          if transacao:
               conta.historico.adicionar_transacao_deposito(self)
               return True
     








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
Sistema bancário.
Digite a opção desejada
[1] Logar na conta
[2] Cadastrar
[3] Abrir conta bancaria
[4] Encerrar programa
#################################

'''

usuario = []
conta = []


data_hora = datetime.now()
data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
data = data_hora_formatada[:10]
hora = data_hora_formatada[11:]


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
          return retorno
     else:
          for usuario in usuario:
               if usuario.cpf == cpf:
                    retorno = True
                    return retorno
               else:
                    retorno = False
     return retorno

def func_logar(usuario,cpf,senha):
     retorno = False
     for usuario in usuario:
               if usuario.cpf == cpf and usuario.senha == senha:
                    retorno = [usuario]
                    return retorno[0]
               else:
                    retorno = False
     
     return retorno




def func_verifica_conta(conta,usuario,numero_conta,agencia,cpf):
     retorno = False
     if usuario.cpf == cpf:
               for conta in conta:
                    if conta.numero == numero_conta and conta.agencia == agencia and numero_conta in usuario.numero_contas:
                         print(f"esse é o obj cliente: {conta._cliente}")
                         print(f"esse é o numero da conta: {conta.numero}")
                         retorno = conta
                         print(f" cliente: {conta.cliente_obj.nome}")
                         return retorno
                    
 
     return retorno




def func_menu_operacao(conta_cliente):
      while True:
                    print(f""" 
                          
Benvindo {conta_cliente.cliente_obj.nome} """)

                    opcao = input(menu)

                    if opcao == "d":

                        valor = float(input("Digite o valor de deposito: "))
  
                        
                        transacao = Deposito(valor)
                        conta_cliente.cliente_obj.realizar_transacao(conta_cliente,transacao)
                        

                    elif opcao == "s":
                       valor = float(input("Digite o valo do saque R$:"))
                       transacao = Saque(valor)
                       conta_cliente.cliente_obj.realizar_transacao(conta_cliente,transacao)


                    elif opcao == "e":
                         extrato = conta_cliente.historico.transacoes
                         if len(extrato) == 0:
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
                              print(f"Saldo total: R$ {conta_cliente.saldo:.2f}")  
                              print("-" * 33)

                    elif opcao == "q":
                       break
                       
                    else:
                        print("Operação inválida,por favor selecione novamente a operação desejada.")        
            
      
def func_main():

     while True:
          global conta
          
    
          opicao_inicial = input(menu1)

          if opicao_inicial == "1":
          
                print("########## Login ##########")

                cpf = input("Digite seu cpf: ")
                agencia = input("Digite a sua agência :")
                numero_conta = int(input("Digite o numero da sua conta: "))
                senha = getpass("Digite sua senha: ")

                cliente = func_logar(usuario,cpf,senha)
                

                if cliente :
                     conta_cliente = func_verifica_conta(conta,cliente,numero_conta,agencia,cpf)
                     if conta_cliente:
                         func_menu_operacao(conta_cliente)

                         
                     else:
                          print("Usuario e senha incorretos")

                else:
                     print("Usuario e senha incorreto")


          elif opicao_inicial == "2":
               print("##########Cadastro##########")
               cpf = input("Digite seu CPF: ")
               verifica = func_verificar_cpf(cpf)

               if verifica == "valido":
                    retorno = func_consulta_cpf(usuario,cpf)

                    if retorno == False:
                          nome = input("Digite seu nome: ")
                          dat_nascimento = input("Data de nascimento: ")
                          endereco = input("""Digite seu endereço no formato:
                                           logradouro,nro - bairro - cidade/sigla estado
                                           """)
                          senha = getpass("Digite a senha ")

                          cliente = PessoaFisica(cpf=cpf,nome=nome,data_nascimento=dat_nascimento,endereco=endereco,senha=senha)
                          usuario.append(cliente)
                          print("Cliente cadastrado com sucesso")
                    else:
                         print("O usuario já existe")       
               else:
                  print("O formato do CPF está invalido, digite somente numeros")

          elif opicao_inicial == "3":
               print("#######< Criar conta >#########")
               cpf = input("Digite seu CPF: ")
               retorno = func_consulta_cpf(usuario,cpf)

               if retorno == True:
                    senha = getpass("Digite sua Senha :")
                    cliente = func_logar(usuario,cpf,senha)
                    if cliente:
                         numero = len(conta) + 1
                         contas = ContaCorrente.nova_conta(cliente=cliente,numero=numero)
                         cliente.adicionar_conta(numero) 
                         conta.append(contas)
                         
                         print(f"Parabéns {cliente.nome} Conta criada com sucesso conta: {contas.numero} agência: {contas.agencia}")
                         

                    else:
                         print("Usuário e senha incorreta 2")

               else:
                    print("Usuário não encontrado,para abrir uma conta é preciso ter cadastro")




          elif opicao_inicial == "4":
              break
          else:
               print("Operação inválida,por favor selecione novamente a operação desejada.")


        
    
     



func_main()