from collections    import defaultdict
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]


assistiram = []
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(len(assistiram))
set(assistiram)
{42, 43, 13, 15, 23, 56}

for usuario in set(assistiram):
    print(usuario)


#conjunto - set - n importa a ordem, diferente da lista que cada um está em uma posicao.


usuarios_data_science1 = {15, 23, 43, 56}
usuarios_machine_learning1 = {13, 23, 56, 42}

usuarios_data_science1 | usuarios_machine_learning1 #ou

usuarios_data_science1 & usuarios_machine_learning1 #e

usuarios_data_science1 - usuarios_machine_learning1 #subtracao

fez_ds_mas_n_fez_ml = usuarios_data_science1 - usuarios_machine_learning1 #verficar a vericidade dos elementos

usuarios_data_science1 ^ usuarios_machine_learning1 #ou exclusivo

usuarios = {1,5,76,34,52,13,17}
usuarios.add(765)

usuarios = frozenset(usuarios) #congela o conjunto de forma a n receber mais dados

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()
set(meu_texto.split()) #remove a duplicidade

#Dicionarios {}
aparicoes = {"Guilherme" : 1,
"cachorro" : 2,
"nome" : 2,
"vindo" : 1}

aparicoes["Guilherme"]
aparicoes.get("Guilherme", 0)

#adicionar elementos
aparicoes["Carlos"] = 2

#deletar elementos
del aparicoes["Carlos"]

#verificar se tem o elemento
"cachorro" in aparicoes

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)


for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

xqdl = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(xqdl)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
meu_texto.split()
aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora +1

print(aparicoes)

from collections    import defaultdict

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora +1
print(aparicoes)


#simplicando

from collections    import defaultdict
from collections    import Counter

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += +1
print(aparicoes)

class Conta():
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]
contas[17]

from collections    import Counter
aparicoes = Counter(meu_texto.split())
print(aparicoes)


#Testando o uso de colecoes contando letras
from collections    import defaultdict
from collections    import Counter
texto1 = """
Erros, exceções, bugs… São palavras bastante presentes na vida de quem desenvolve softwares. Um grande desafio é conseguir detectar os bugs, descobrir o que causou, em qual parte do aplicativo eles ocorreram, e corrigi-los quanto antes! Mas a maior dificuldade é saber que um bug ocorreu, pois, muitas vezes os usuários não reportam. Ou, ainda, quando reportam não têm o conhecimento técnico de programação para enviar informações detalhadas do que pode ter causado o erro. Para resolver isso, podemos utilizar o Firebase Crashlytics! Com ele, teremos relatórios precisos sobre erros e comportamentos inesperados que ocorram no app.
Firebase Crashlytics
O Firebase Crashlytics é uma solução de relatórios criada pela Google para reportar falhas em aplicações iOS, Android e Unity. É uma ferramenta que cria relatórios de falhas em tempo real para ajudar a monitorar, priorizar e corrigir problemas de estabilidade que possam comprometer a qualidade do seu aplicativo. O Crashlytics economiza um enorme tempo na solução de problemas, através do agrupamento inteligente de falhas e do mapeamento das circunstâncias que levam à elas. Conseguimos utilizar o Crashlytics no Flutter a partir do pacote firebase_crashlytics.
Preparação do Firebase
Primeiro, você precisa ter uma conta Google (Gmail), que será utilizada para acessar o console de desenvolvedor do Firebase. Para isso, acesse: https://firebase.google.com/ e clique em “Ir para o console”.
"""
texto2 = """
Uma das grandes vantagens de implementar esse tipo de notificação em seu aplicativo é poder monitorar a porcentagem de usuários que recebem, abrem, ignoram etc. as suas notificações. Desta maneira é possível mapear quais campanhas publicitárias fazem mais sentido de acordo com um determinado público. Essa abordagem de fazer com que o aplicativo seja receptor, isto é, fique esperando requisições, chamamos de Push Notification. Atualmente, existem algumas plataformas que oferecem esses serviços mensageiros, como o FCM (Firebase Cloud Messaging).
Configurando o Firebase
"""
Counter(texto1.lower())
Counter(texto2.lower())

aparicoes1 = Counter(texto1.lower())
total_de_aparicoes1 = sum(aparicoes1.values())
print("Total de letras no Texto1 é {}".format(total_de_aparicoes1))

aparicoes2 = Counter(texto2.lower())
total_de_aparicoes2 = sum(aparicoes2.values())
print("Total de letras no Texto2 é {}".format(total_de_aparicoes2))

print("              ")
print("              ")
print("              ")


def analisa_frequencia_de_letras(texto):
    aparicoes1 = Counter(texto.lower())
    total_de_aparicoes1 = sum(aparicoes1.values())
    proporcoes = [(letra, frequencia1 / total_de_aparicoes1) for letra, frequencia1 in aparicoes1.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao *100))

analisa_frequencia_de_letras(texto1)

print("              ")
print("              ")
print("              ")

analisa_frequencia_de_letras(texto2)


