#while True:
   # numero = int(input('Informe um numero: '))

   # if numero == 10:
   #     break 

  #  print(numero)


# for numero in range(100):
    #if numero ==10:
       # break # Vai para a execução quando o if for atendido
   # print(numero, end=' ')   

#for numero in range(100):
    #if numero ==50:
    #    continue # uma versão oposta ao break
   # print(numero, end=' ') 

## while junto com if 

while True:
    numero= int(input('Informe um número: '))

    if numero % 2 == 0:
        continue
    
    if numero == 10:
        break 

    print(numero)  

### Para cortar é necessário que o break venha primeiro que o continue    
# 
# while True:
   #  numero= int(input('Informe um número: '))
    # if numero == 10:
       #  break 

    # if numero % 2 == 0:
       #  continue
    
   #  print(numero)      