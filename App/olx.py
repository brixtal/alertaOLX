import urllib2
from HTMLParser import HTMLParser

class Olx:

    ##Constantes##
    __tagQtdTotal = 'class="qtd">'
    __tagInicioListaAnuncios = '<ul class="list" id="main-ad-list">'
    __marcadorLinkAnuncio = 'href="'
    __marcadorTituloAnuncio = '<h3 class="OLXad-list-title mb5px">'
    __marcadorInfosAdicionais = '<p class="text detail-specific">'
    __marcadorPrecoAnuncio = '<p class="OLXad-list-price">'
    __marcadorDataAnuncio = '<p class="text mb5px">'
    __marcadorHoraAnuncio = '<p class="text mb5px">'
    __indicadorReducaoPreco = '<img class="icon-red-arrow"'
    __marcadorFimAnuncio = '</li>'
    
    
    def getHtml(self, url):
        request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/57.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://thewebsite.com",
        "Connection": "keep-alive" 
        }

        request = urllib2.Request(url, headers=request_headers)
        contents = urllib2.urlopen(request).read()

        return contents

    def getTagQtdTotal(self):
        return self.__tagQtdTotal
    def getTamanhoTagQtdTotal(self):
        return len(self.__tagQtdTotal)
    def getTagInicioListaAnuncios(self):
        return self.__tagInicioListaAnuncios
    def getTamanhoTagInicioListaAnuncios(self):
        return len(self.__tagInicioListaAnuncios)
    def getMarcadorLinkAnuncio(self):
        return self.__marcadorLinkAnuncio
    def getTamanhoMarcadorLinkAnuncio(self):
        return len(self.__marcadorLinkAnuncio)
    def getMarcadorTituloAnuncio(self):
        return self.__marcadorTituloAnuncio
    def getTamanhoMarcadorTituloAnuncio(self):
        return len(self.__marcadorTituloAnuncio)
    def getMarcadorInfosAdicionais(self):
        return self.__marcadorInfosAdicionais
    def getTamanhoMarcadorInfosAdicionais(self):
        return len(self.__marcadorInfosAdicionais)
    def getMarcadorPrecoAnuncio(self):
        return self.__marcadorPrecoAnuncio
    def getTamanhoMarcadorPrecoAnuncio(self):
        return len(self.__marcadorPrecoAnuncio)
    def getMarcadorDataAnuncio(self):
        return self.__marcadorDataAnuncio
    def getTamanhoMarcadorDataAnuncio(self):
        return len(self.__marcadorDataAnuncio)
    def getMarcadorHoraAnuncio(self):
        return self.__marcadorHoraAnuncio
    def getTamanhoMarcadorHoraAnuncio(self):
        return len(self.__marcadorHoraAnuncio)
    def getIndicadorReducaoPreco(self):
        return self.__indicadorReducaoPreco
    def getTamanhoIndicadorReducaoPreco(self):
        return len(self.__indicadorReducaoPreco)
    def getMarcadorFimAnuncio(self):
        return self.__marcadorFimAnuncio
    def getTamanhoMarcadorFimAnuncio(self):
        return len(self.__marcadorFimAnuncio)
