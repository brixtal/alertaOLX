# Para que você nunca perca um anúncio!

A ideia de criar esse sistema de código aberto surgiu com a dificuldade de acompanhar a evolução dos anúncios de produtos que eu desejava comprar na OLX Brasil. Dentre os milhares de novos produtos anunciados na OLX todos os dias, existem grandes oportunidades que geralmente não ficam mais do que poucas horas no mural de anúncios. Para não deixar que ofertas com essa sumam, o **alertaOLX** busca enviar para você e-mails de alerta com o resumo das últimas ofertas anunciadas no site. Dessa forma você poderá acompanhar de uma forma muito mais simples as novas ofertas e ainda terá uma forma de guardar as informações de uma maneira muito mais prática.


# Como funciona o sistema?

A proposta é muito simples:
* Copie a URL da página de exibição dos anúncios já com os filtros que você desejar;
* Passe a URL como parâmetro de execução do script em Python 2.7.14;
* Utilize o agendador do seu sistema operacional para executar o **alertaOLX** de tempos em tempos;
* Pronto! Você receberá um e-mail sempre que houver um novo anúncio com os parâmetros da sua pesquisa! 

# Como configurar o sistema alertaOLX?
O **alertaOLX** foi escrito em Python e pode ser executado tanto em Windows, quanto em Linux.
Para executá-lo, siga os seguintes passos:
* Instale o Python 2.7.14
	* Para Windows, baixe o executável em https://www.python.org/downloads/release/python-2714/
	* Para Linux, siga os passos descritos em https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/
* Baixe o código-fonte do **alertaOLX**, colocando-o no diretório que preferir;
* Para executar o sistema, faça a chamada tradicional do Python, passando como parâmetros o local do arquivo main.py (contido no diretório App), e a URL da OLX já com os parâmetros do filtro que você desejar.
Por exemplo:
```
python2.7 main.py 'http://rj.olx.com.br/imoveis/venda?gsp=3&pe=900000&ps=200000&roe=4&ros=2&se=7&ss=1'
```
## Para agendamento utilizando o crontab do Linux
Se optar por utilizar o sistema no Linux, uma das maneiras de realizar a automatização do script é através do crontab. Para configurá-lo, você deve:
* Executar o comando
```
crontab -e
```
* Colocar os parâmetros de agendamento, seguido do comando a ser executado, como no exemplo abaixo:
```
0 * * * 1-4 /home/ubuntu/alertaOLX/main.py 'http://rj.olx.com.br/imoveis/venda?gsp=3&pe=900000&ps=200000&roe=4&ros=2&se=7&ss=1'
*/15 * * * 5-6 /home/ubuntu/alertaOLX/main.py 'http://rj.olx.com.br/imoveis/venda?gsp=3&pe=900000&ps=200000&roe=4&ros=2&se=7&ss=1'
*/30 * * * 7 /home/ubuntu/alertaOLX/main.py 'http://rj.olx.com.br/imoveis/venda?gsp=3&pe=900000&ps=200000&roe=4&ros=2&se=7&ss=1'

```
> No exemplo acima, a primeira linha faz com que o agendador execute o sistema de alerta de segunda a quinta, de hora em hora; a segunda linha faz com que seja executado sábado e domingo a cada 15 minutos; e a última linha faz com que o sistema seja executado a cada 30 minutos aos domingos. Mais detalhes de como usar o crontab pode ser encontrado em https://canaltech.com.br/linux/cron-facilite-o-agendamento-de-tarefas-no-linux/

OBS: Não tive a oportunidade de testar em MacOS, mas creio que não sejam necessárias modificações para a execução, pricipalmente porque o sistema já roda sem precisar de moficação no Linux.

# Por que em Python 2.7 e não em Python 3?

Esse sistema começou como uma forma de aprender a linguagem Python para a realização de uma prova, cuja ementa exigia a aplicação de Python 2.7. Em breve será lançada a atualização do **alertaOLX** para Python 3.6.

# Por que commits em português?

Como esse é um sistema majoritariamente usado por brasileiros, nada mais justo que suas informações e código sejam escritos em pt-br. Com isso espera-se que seus usários consigam utilzar o sistema de maneira simples, principalmente para usuários que não tenham tanto domínio de programação e queiram entender o funcionamento do código. Viva o bom português! ;-)