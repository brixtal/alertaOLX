# encoding: utf-8
import urllib2
from HTMLParser import HTMLParser
from olx import Olx
from anuncio import Anuncio
from datetime import *
from myemail import MyEmail
import sys

offset = 0

#url = "http://rj.olx.com.br/imoveis?"

url = sys.argv[1]

url = url + "&o="

olx = Olx()

anuncio = Anuncio()

pagina = olx.getHtml(url+str(offset))

indice = pagina.find(olx.getTagQtdTotal()) + olx.getTamanhoTagQtdTotal()

char = ''
qtdAnuncios = ''
while char != '<':
    char = pagina[indice]
    if char >= '1' and char <= '9':
        qtdAnuncios += char
    indice += 1

qtdAnunciosPorPagina = 50
qtdAnuncios = int(qtdAnuncios)
qtdPaginas = int(qtdAnuncios/qtdAnunciosPorPagina)

ultimaAtualizacao = open("../sysout/ultimaAtualizacao.out", 'r')

ultimaAtualizacaoStr = ultimaAtualizacao.read(13)

ultimaAtualizacao.close()
print ultimaAtualizacaoStr
ultimaAtulizacao = datetime.strptime(ultimaAtualizacaoStr, '%Y%m%d%H:%M')
anunciosNovos = 0
email = open("../sysout/anuncioOLX.out", 'w')
print qtdPaginas
while offset <= qtdPaginas:
    
    print "[Mensagem] Abrindo pagina #", str(offset+1)

    pagina = olx.getHtml(url+str(offset))
    
    indice = pagina.find(olx.getTagInicioListaAnuncios()) + olx.getTamanhoTagInicioListaAnuncios()

    pagina = pagina[indice:]

    i = 0
    limitador = qtdAnunciosPorPagina
    if(qtdAnuncios < qtdAnunciosPorPagina):
        limitador = qtdAnuncios
    while i in range(0,limitador):
        print "[Mensagem] Lendo anuncio #", str(i+1)
        anuncio.linkAnuncio = anuncio.obterLinkAnuncio(pagina)

        anuncio.tituloAnuncio = anuncio.obterTituloAnuncio(pagina)

        anuncio.infosAdicionais = anuncio.obterInfosAdicionais(pagina)

        anuncio.precoAnuncio = anuncio.obterPrecoAnuncio(pagina)

        anuncio.dataHoraAnuncio = anuncio.obterDataHoraAnuncio(pagina)
        if(anuncio.dataHoraAnuncio <= ultimaAtulizacao):
            if(i == 0 and offset == 0):
                print "[Mensagem] Sem novos anuncios."
            offset = qtdPaginas            
            i = 50
            
        else:
                email.write(anuncio.tituloAnuncio)
                email.write('\n')
                email.write(anuncio.linkAnuncio)
                email.write('\n')
                email.write(anuncio.infosAdicionais)
                email.write('\n')
                email.write(anuncio.precoAnuncio)
                email.write('\n')
                email.write(anuncio.dataHoraAnuncio.strftime("%d/%m/%Y %H:%M"))
                email.write('\n')
                email.write('\n')
                anunciosNovos += 1

        if(offset == 0 and i == 0):
            configuracao = open("../sysout/ultimaAtualizacao.out", 'w')
            configuracao.write(anuncio.dataHoraAnuncio.strftime("%Y%m%d%H:%M"))
            configuracao.close()
        
        indice = pagina.find(olx.getMarcadorFimAnuncio()) + olx.getTamanhoMarcadorFimAnuncio()

        pagina = pagina[indice:]   

        i+=1
    offset += 1
email.close()


if anunciosNovos >= 1:
        mensagem = open("../sysout/anuncioOLX.out", 'r')
        myEmail = MyEmail()
        myEmail.enviarEmail(mensagem.read(100000))
        mensagem.close()
