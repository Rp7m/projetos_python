from datetime import datetime

menu = ''''
#################################
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
#################################
'''
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

data_hora = datetime.now()
data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
data = data_hora_formatada[:10]
hora = data_hora_formatada[11:]
indice = 0
ultima_operacao = 0

                        




while True:

    if len(extrato) != 0:
            ultima_operacao = len(extrato) - 1
        
    
    opcao = input(menu)

    if opcao == "d":

        entrada = input("Digite o valor de deposito: ")
        if "," in entrada:
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
        
        
        


    elif opcao == "s":

        if numero_saques == LIMITE_SAQUE and extrato[ultima_operacao][0] == data:
                print("Limite de saque diário estourado")
        else:
            entrada = input("Digite o valo do saque R$:")
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
                    print("Operação não realiza valor maior que o limite diário ou valor invalido.")
        


        

    elif opcao == "e":
        lista = len(extrato)
        if lista == 0:
             print("Não foram realizadas movimentações")
             
        else:
            titulo1 = "Data"
            titulo2 = "Horario"
            titulo3 = "Operação"
            print(titulo1.center(12,"-")+titulo2.center(11,"-")+titulo3.center(10,"-"))
            
            for dados in extrato:
                
                d = extrato[indice][0] # Data de deposito
                h = extrato[indice][1] # Hora hora de deposito
                dep = str(extrato[indice][2]) # Deposito
                print(d.center(12)+h.center(11)+dep.center(10))
                indice += 1
              
            
            
            indice = 0 
            
            print("-" * 33)
            print(f"Saldo total: R$ {saldo:.2f}")  
            print("-" * 33)
            

    elif opcao == "q":
        break
    else:
        print("Operação inválida,por favor selecione novamente a operação desejada.")