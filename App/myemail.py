import smtplib
from readConfig import ReadConfig

class MyEmail:        

        def enviarEmail(self, mensagem):

                clas = ReadConfig()
                config = clas.getConfig('../config/email.private')
                smtp = smtplib.SMTP(config.get('smtp'), config.get('port'))
                smtp.starttls()
                smtp.login(config.get('user'), config.get('password'))

                de = config.get('from')
                para = [config.get('to')]
                
                msg = """From: %s
To: %s
Subject: %s

%s

""" % (config.get('alias'), ', '.join(para), config.get('subject'), mensagem)

                print msg
        
                smtp.sendmail(de, para, msg)

                smtp.quit()
