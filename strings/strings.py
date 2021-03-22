from ExtratorArgumentosUrl import ExtratorArgumentosUrl
url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)

print(argumentosUrl == argumentosUrl2)

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()

print(moedaDestino, moedaOrigem, valor)
print(argumentosUrl)
print(id(argumentosUrl))
print(id(argumentosUrl2))



#index = url.find("moedadestino") + len("moedadestino") +1
#substring = url[index:]
#print(substring)

