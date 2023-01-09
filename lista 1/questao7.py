"""Exercite seus conhecimentos, crie um programa capaz de consultar um nome de domínio e obtenha várias páginas web.

Para isso, crie uma função em python3 que utilize a biblioteca:

import http.client
A função deve ter o cabeçalho e os parâmetros definidos como:

def HTTPclient(host,port)
Onde os parâmetros "host" é um endereço IP informado como string e "port" é um inteiro positivo que representa a porta onde o serviço de rede para páginas web está hospedado. Ambos os parâmetros não precisam ser recebidos por entrada de dados, a rotina principal irá instanciá-los, o esforço deve ser única e exclusivamente desempenhado para criar a função HTTPclient().

Dica:

Utilize um conector como abaixo:

conn = http.client.HTTPConnection(host, port)

Entradas

O programa receberá uma variável inteira L (1≤L≤20) que representa o número total de conteúdos (objetos) a serem consultados na internet.

Em seguida, serão informados L nomes de conteúdos que devem ser obtidos (campo url do http), os quais deverão ser consultados 1 à 1. A medida em que as conexões para o servidor forem sendo feitas, o conteúdo dos objetos recuperados precisam ser impressos.

As variáveis "L" e "conteúdo" (content), precisam ser instanciadas por entrada de dados. Para isso, utilize a função input() do python (em C, seria a scanf()) para instanciar as variáveis "L" e "content" como abaixo:

L = int(input())
content = input()

Saída

O conteúdo de cada um dos arquivos (objetos) consultados (recuperados) deverá ser impresso na tela após decodificados, para isso, utilize a função .decode() dos dados obtidos por um request.

Input: 
1
index.html

Result:
<HTML>
    <HEADER>
        <TITLE>Teste</TITLE>
    </HEADER>
    <BODY>TD é demais</BODY>
</HTML>
"""

import http.client

def HTTPclient(host, port):
    conn = http.client.HTTPConnection(host, port)
    L = int(input())
    for _ in range(L):
        content = input()
        conn.request("GET", content)
        print(conn.getresponse().read().decode())
