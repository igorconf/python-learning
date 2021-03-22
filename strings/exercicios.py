import re
argumento = "www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar"

url = "pagina?argumentos"

index = argumento.find("?")
print(argumento[index +1:])

nome         = "Rodrigo"
sobreNome     = ""

if nome:
    print("Nome Correto")
else:
    print("Nome Incorreto")

if sobreNome:
    print("Sobrenome Correto")
else:
    print("Sobrenome Incorreto")
####

    nome = 'Eren Yeager'
    tamanho = len(nome)
    indice = nome.find('Eren')
    print(tamanho)
    print(nome[indice:tamanho])

episodio = "Boku no hero - TEmporada 1, episódio 12"
episodioFormatado = episodio.lower().replace("episódio ","ep").upper().replace("temporada ", "s")

print(episodioFormatado)


padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"

retorno = re.findall(padrao, conversa3)
print(retorno)


class Quadrado:
    def __init__(self,nome,lado):
        self.nome = nome
        self.lado = lado
    def __str__(self):
        return "nome = {} Lado ={}".format(self.nome,self.lado)

quadradinho = Quadrado("Meu Quadrado",2)
print(quadradinho)

