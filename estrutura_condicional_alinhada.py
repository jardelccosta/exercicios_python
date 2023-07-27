conta_noraml = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1800

cheque_especial = 450

if conta_noraml:
    
    if saldo >=saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial")
    else:
        print("Não foi possivel realizado o saque, saldo insuficiente")    

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque reliazado com sucesso") 
    else:
        print("Saldo Insuficiente") 

elif conta_especial:
        print("Conta especial selecionada")                  

else:
      print("Sistema não reconheceu o tipo de conta, entre em contato com seu gerente.")        
