class Collections:

    idade1 = 39
    idade2 = 30
    idade3 = 27
    idade4 = 18

    print(idade1)
    print(idade2)
    print(idade3)
    print(idade4)

    idades = [39, 30, 27, 18]

    for idade in idades:
        print(idade)

##deixar salvo tudo q fiz pelo python console!

from Collections.Introdução import Collections

39
30
27
18
39
30
27
18
idades
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'idades' is not defined
idades = [39, 30, 27, 18, 15]
idades
[39, 30, 27, 18, 15]
idades.remove(30)
idades
[39, 27, 18, 15]
len(idades)
4
28 in idades
False
15 in idades
True
if 15 in idades:
    idades.remove(15)
idades
print(idades)
[39, 27, 18]
if 28 in idades:
    idades.remove(28)
else:
    idades.append(28)

idades
[39, 27, 18, 28]
idades.insert(0, 20)
idades
[20, 39, 27, 18, 28]
idades.append([46, 48])
for elemento in idades:
    print("Recebi o elemento", elemento)

Recebi
o
elemento
20
Recebi
o
elemento
39
Recebi
o
elemento
27
Recebi
o
elemento
18
Recebi
o
elemento
28
Recebi
o
elemento[46, 48]
idades = [20, 39, 18]
idades.extend(25, 35, 49, 50)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: list.extend()
takes
exactly
one
argument(4
given)
idades.extend([25, 35, 49, 50])
idades
[20, 39, 18, 25, 35, 49, 50]
idades_ano_q_vem = []
for idade in idades:
    idades_ano_q_vem.append(idade + 1)

idades_ano_q_vem
[21, 40, 19, 26, 36, 50, 51]
idades_ano_q_vem[(idade + 1)
for idade in idades]

idades_ano_q_vem
File
"<input>", line
1
idades_ano_q_vem[(idade + 1)
for idade in idades]
^
SyntaxError: invalid
syntax
idades_ano_q_vem
[21, 40, 19, 26, 36, 50, 51]
idades_ano_q_vemm = [(idade + 1) for idade in idades]
idades_ano_q_vemm
[21, 40, 19, 26, 36, 50, 51]
maioridade = [(idade) for idade in idades if idade > 21]
maioridade
[39, 25, 35, 49, 50]


def faz_processamento_de_visualizacao(lista):
    print(len(lista))


faz_processamento_de_visualizacao(idades)
7
faz_processamento_de_visualizacao(idades)
idades
7
idades
[20, 39, 18, 25, 35, 49, 50]


def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13)




