from olx import Olx
from datetime import datetime, timedelta

class Anuncio:
    codigoAnuncio = ''
    tituloAnuncio = ''
    linkAnuncio = ''
    infosAdicionais = ''
    precoAnuncio = ''
    dataHoraAnuncio = ''
    indicadorReducaoPreco = 0
    global olx
    olx = Olx()
    global meses
    meses = {'Jan':'01', 'Fev':'02', 'Mar':'03', 'Abr':'04', 'Mai':'05', 'Jun':'06', 'Jul':'07', 'Ago':'08', 'Set':'09', 'Out':'10', 'Nov':'11', 'Dez':'12'}

    def __init__(self):
        pass

    def getTexto(self,pagina, indice, limitador = '<'):
		texto = ''
		char = ''
		while char != limitador:
			char = pagina[indice]
			if char != '\n' and char != '\r' and char != '\t':
				texto += char
			indice += 1
		texto = texto[:len(texto)-1]		
		return texto.strip()

    def limpaLink(self,texto):
		indice=0
		char = ''
		link = ''
		ignore = False
		print texto
		print len(texto)
		while indice < len(texto):
                    print indice
                    
		    char = texto[indice]
                    if ignore == False:	
			if char != '?':
                            link += char
                        else :
                            print "Peguei ?"
                            return link.strip()            
		    indice += 1
		return link.strip()

    
    def obterLinkAnuncio(self, pagina):
        indice = pagina.find(olx.getMarcadorLinkAnuncio()) + olx.getTamanhoMarcadorLinkAnuncio()
        texto = self.getTexto(pagina, indice, '"')        
        return self.limpaLink(texto.strip())
		

    def obterTituloAnuncio(self, pagina):
        indice = pagina.find(olx.getMarcadorTituloAnuncio()) + olx.getTamanhoMarcadorTituloAnuncio()
        return self.getTexto(pagina, indice)

    def obterInfosAdicionais(self,pagina):
        indice = pagina.find(olx.getMarcadorInfosAdicionais()) + olx.getTamanhoMarcadorInfosAdicionais()
        return self.getTexto(pagina, indice)
    
    def obterPrecoAnuncio(self,pagina):
        indice = pagina.find(olx.getMarcadorPrecoAnuncio()) + olx.getTamanhoMarcadorPrecoAnuncio()
        return self.getTexto(pagina, indice)

    def obterDataHoraAnuncio(self,pagina):
        dia = datetime.now()
        day = ''
        mes = ''
        ano = ''
        data = ''
        indice = pagina.find(olx.getMarcadorDataAnuncio()) + olx.getTamanhoMarcadorDataAnuncio()
        texto = self.getTexto(pagina, indice)
        
        if (texto == "Ontem"):
            dia = datetime.now() - timedelta(days=1)
        elif (texto == "Hoje"):
              dia = datetime.now()
        else:
            ano = str(datetime.now().strftime('%Y'))
            day = texto.split()[0]
            mes = meses.get(texto.split()[1])

            dia = datetime.strptime(day+mes+ano, '%d%m%Y')

            if (dia > datetime.now()):
                ano = str(int(ano)-1)
                day = texto.split()[0]
                mes = meses.get(texto.split()[1])
                dia = datetime.strptime(day+mes+ano, '%d%m%Y')
        
        pagina = pagina[indice:]
        indice = pagina.find(olx.getMarcadorHoraAnuncio()) + olx.getTamanhoMarcadorHoraAnuncio()
        texto = self.getTexto(pagina, indice)
        
        data = dia.strftime("%Y%m%d")
        dia = datetime.strptime(data+texto, '%Y%m%d%H:%M')
        return dia


