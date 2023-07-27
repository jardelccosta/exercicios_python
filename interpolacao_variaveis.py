## O modelo com % não é tão utilizado mais 

nome = "Jardel"
idade = 29
profissao = "Estudante"
linguagem =  "Python"

print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))

# O método format já é mais utilizado
nome = "Jardel"
idade = 29
profissao = "Estudante"
linguagem =  "Python"

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

nome = "Jardel"
idade = 29
profissao = "Estudante"
linguagem =  "Python"

print('Olá, me chamo {2}. Eu tenho {0} anos de idade, trabalho com {1} e estou matriculado no curso de {3}.'.format(idade, profissao, nome, linguagem ))

nome = "Jardel"
idade = 29
profissao = "Estudante"
linguagem =  "Python"

print('Olá, me chamo {nome}. Eu tenho {idadee} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.'.format(idadee=idade, profissao=profissao, nome=nome, linguagem=linguagem ))

dados = {'nome': "Guilherme", "idade":30, "profissao":'estudante', 'linguagem':'Python'}
print('Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.'.format(**dados))

## f-string é mais outro modelo e deixa mais limpo 

nome = "Jardel"
idade = 29
profissao = "Estudante"
linguagem =  "Python"

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.')

dados = {'nome': "Matheus", "idade":30, "profissao":'estudante', 'linguagem':'Python'}
print (f'Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.')

## Formannto strings com f-string
PI = 3.14159
print(f'Valor do PI: {PI:.2f}')
print(f'Valor de Pi: {PI:10.2f} ')

