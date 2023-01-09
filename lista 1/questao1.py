"""
Você sabe o que é uma consulta de DNS reverso?

A maioria das pessoas conhece a utilização do DNS (Domain Name Server) em sua forma padrão: transformar um domínio em um endereço IP. O DNS Reverso faz exatamente o contrário: a partir de um endereço IP determina-se o domínio associado.

Com este contexto em mente, implemente um programa que seja capaz de ler uma quantidade L de endereços IPs e, a partir de cada endereço, faça uma consulta a um sistema de nomes (Domain Name System) da internet. A partir da consulta, recupere os nomes de domínios (Domain Names) dos IPs acessados e imprima-os na tela. 

Utilize a biblioteca socket e a função socket.gethostbyaddr().

Entradas
Valor inteiro L=(0≤L≤10000) que representa o número de IPs a serem lidos e consultados. Em seguida, o programa deverá ler L endereços IPs separados um por linha.

Os valores das variáveis "L" e "IP" serão lidos da entrada padrão no programa. Para isso, utilize a função input() do python (em C, seria a scanf()) para instanciar as variáveis "L" e "IP" como abaixo:

L = int(input())
IP = input()
Saída

Você deverá imprimir os nomes de domínio (domain names) ligados aos IPs de entrada.

*Obs: Na linguagem python, a conversão do valor lido na entrada padrão (input()) para um valor inteiro deve ser feita através de um cast de dados, usando para isso a função int()

Exemplo:

variavel = int(input())

Input:
4
143.54.2.20
143.54.11.34
200.160.2.3
200.160.4.2

Result:
www.ufrgs.br
www.inf.ufrgs.br
registro.br
cgi.br
"""

import socket

hostname_list = []
L = int(input())
for _ in range(L):
    IP = input()
    hostname_list.append(socket.gethostbyaddr(IP)[0])

for hostname in hostname_list:
    print(hostname)
