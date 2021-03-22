import numpy as np
from abc import ABCMeta, abstractmethod
from operator import attrgetter


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()
    print(conta)

from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<".format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass



#isinstance(ContaCorrente(34), Conta)

idades = [15, 87, 65, 56, 32, 49, 37]
for idade in idades:
    print(idade)

15
87
65
56
32
49
37
idades = [15, 87, 32, 65, 56, 32, 49, 37]
range(len(idades))
range(0, 8)
for i in range(len(idades))
    print(i)

File
"<input>", line
1
for i in range(len(idades))
    ^
    SyntaxError: invalid
    syntax
    for i in range(len(idades)):
        print(i, idades[i])

    0
    15
    1
    87
    2
    32
    3
    65
    4
    56
    5
    32
    6
    49
    7
    37
    enumerate(idades)
    < enumerate
    object
    at
    0x000002051AF10A00 >
    list(enumerate(idades))
    [(0, 15), (1, 87), (2, 32), (3, 65), (4, 56), (5, 32), (6, 49), (7, 37)]
    for indice, idade in enumerate(idades):
        print(indice, "x", idade)

    0
    x
    15
    1
    x
    87
    2
    x
    32
    3
    x
    65
    4
    x
    56
    5
    x
    32
    6
    x
    49
    7
    x
    37
    usuarios = [("Guilherme", 37, 1981), ("Daniela", 31, 1987), ("Paulo", 39, 1979)]
    for nome, idade, nascimento in usuarios:
        print(nome)

    Guilherme
    Daniela
    Paulo
    for nome, idade, nascimento in usuarios:
        print(nome)
        print(nome, idade)

    Guilherme
    Guilherme
    37
    Daniela
    Daniela
    31
    Paulo
    Paulo
    39
    print(idade, nascimento)
    39
    1979
    for nome, idade, nascimento in usuarios:
        print(nome)
        print(nome, idade)
        print(nascimento, idade)
        
idades
[15, 87, 32, 65, 56, 32, 49, 37]
usuarios
[('Guilherme', 37, 1981), ('Daniela', 31, 1987), ('Paulo', 39, 1979)]
sorted(idades)
[15, 32, 32, 37, 49, 56, 65, 87]
reversed(idades)
<list_reverseiterator object at 0x000002051AE85670>
list(reversed(idades))
[37, 49, 32, 56, 65, 32, 87, 15]
        
    sorted(idades, reverse=True)
[87, 65, 56, 49, 37, 32, 32, 15]
list(reversed(sorted(idades)))
[87, 65, 56, 49, 37, 32, 32, 15]


from operator import attrgetter
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)
    
    
    
    
conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)
conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)
conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)
contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
conta_do_guilherme < conta_da_daniela
True
conta_do_guilherme > conta_da_daniela
False
sorted(contas)
[<__main__.ContaSalario object at 0x000002169EFE30A0>, <__main__.ContaSalario object at 0x000002169EFE3220>, <__main__.ContaSalario object at 0x000002169EFE3130>]
for conta in sorted(contas):
    print(conta)
    
[>>Codigo 17 Saldo 500<<
[>>Codigo 133 Saldo 510<<
[>>Codigo 3 Saldo 1000<<
for conta in sorted(contas, reverse=True):
    print(conta)
    
[>>Codigo 3 Saldo 1000<<
[>>Codigo 133 Saldo 510<<
[>>Codigo 17 Saldo 500<<
