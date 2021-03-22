import re
import requests
from cpf_cnpj import Documento
from validate_docbr import CPF
from validate_docbr import CNPJ
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from datetime import datetime, timedelta
from acesso_cep import BuscaEndereco


#exemplo_cpf = "05892574717"
#exemplo_cnpj = "35379838000112"
#documento = Documento.cria_documento(exemplo_cnpj)
#documento1 = Documento.cria_documento(exemplo_cpf)

#print(documento1)
#print(documento)

#padrao = "[0-9][a-z]{2}[0-9]"
#texto = "123 1ax2 1cc aa1"
#resposta = re.search(padrao, texto)
#print(resposta.group())

#padrao = "\w{5,50}@\w{3,10}.\w{2,3}"
#texto = "oaskdoasokdasodokals igorconf@hotmail.com dkoasdkoasokdakosdkoaskodsao"
#resposta = re.search(padrao, texto)
#print(resposta.group())

#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "eu gosto do numero 2126451234"
#resposta = re.findall(padrao, texto)
#print(resposta)


#telefone = "5522988577278"
#telefone_objeto = TelefonesBr(telefone)
#print(telefone_objeto)


#cadastro = DatasBr()
#print(cadastro)


#hoje = DatasBr()
#print(hoje.tempo_cadastro())


cep = "01001000"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(type(r.text))

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

