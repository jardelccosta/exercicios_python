### primeiro modelo - IF
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade>=18:
    print("Maior de idade, pode tirar a CNH.")
if idade<MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")  

### segundo modelo - else

if idade>=18:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")  

# terceiro modelo - ilse
if idade>=18:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode aulas práticas.")    
else:
    print("Ainda não pode tirar a CNH.") 

