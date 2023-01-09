"""
Exercite seus conhecimentos, crie um programa capaz de consultar um nome de domínio e obtenha através de uma conexão HTTP, conteúdos on-line e, de acordo com o tipo do conteúdo, imprima na tela uma ação diferente.

Crie uma função em python3 que utilize a biblioteca:

import http.client
A função deve ter o cabeçalho e os parâmetros definidos como:

def HTTPclient(host,port)
Onde os parâmetros "host" é um endereço IP informado como string e "port" é um inteiro com a porta onde o serviço de rede para páginas web está hospedado. Ambos os parâmetros não precisam ser recebidos por entrada de dados, a rotina principal irá instanciá-los, o esforço deve ser único e exclusivamente desempenhado para criar a função HTTPclient().

Dica:

Utilize a função oriunda da classe HTTPResponse, getheaders() (https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse) para se obter o cabeçalho da mensagem HTTP.

Exemplo:

conn = http.client.HTTPConnection(host, port)

conn.request("GET",content)

r1 = conn.getresponse()

data1 = r1.getheaders()       

Para realizar esse exercício, consulte a RFC "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content" em https://tools.ietf.org/html/rfc7231#section-3.1.1.5

Entrada

O programa receberá uma variável inteira L ([[1 \le L \le 20]]) informando o total de conteúdos a serem consultados. A seguir, L nomes de conteúdos que devem ser recuperados do servidor web, os quais deverão ser consultados 1 à 1. Seguindo os tipos definidos na tabela abaixo, consulte e imprima as mensagens de saída no formato definido, de acordo com os tipos dos conteúdos recuperados. Veja a descrição em maiores detalhes na seção Saída.

As variáveis "L" e "conteúdo" (content), precisam ser instanciadas por entrada de dados. Para isso, utilize a função input() do python (em C, seria a scanf()) para instanciar as variáveis "L" e "content" como abaixo:

L = int(input())
content = input()

Saída

Uma mensagem, por linha, conforme a definição de tipo apresentado na tabela abaixo.

Tipo	Mensagem
audio/mpeg	Playing audio: $conteúdo
text/html	Browsing: $conteudo
video/x-msvideo	Playing media: $conteudo
application/json	Processing JSON: $conteudo
Formato desconhecido	Unknown file/media: $tipo_conteudo-$conteudo
Conteúdo indisponível	Content not found

Input:
5
index.html
content.json
media.avi
music.mp3
this_does_not_exist

Result:
Browsing: index.html
Processing JSON: content.json
Playing media: media.avi
Playing audio: music.mp3
Content not found
"""

import http.client

content_dict = {
    'audio/mpeg': 'Playing audio:',
    'text/html': 'Browsing:',
    'video/x-msvideo': 'Playing media:',
    'application/json': 'Processing JSON:',
    }

def HTTPclient(host, port):
    conn = http.client.HTTPConnection(host, port)
    L = int(input())
    for _ in range(L):
        content = input()
        conn.request("GET",content)
        r1 = conn.getresponse()
        data1 = r1.getheaders()
        content_type = data1[2][1]
        if content_type == 'close':
            print('Content not found')
        elif content_dict.get(content_type) != None:
            print(content_dict.get(content_type), content)
        else:
            print('Unknown file/media:', content_type+'-'+content)
