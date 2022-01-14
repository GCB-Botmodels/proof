#para guardar una variable y su valor en el entorno
SENDER_PASS = ''

#luego se recupera de este modo
import smtplib
import os
from email.mime.text import MIMEText
from typing import no_type_check

emisor = "bot01alerta@gmail.com"
receptor = "cabigerman@gmail.com"

#Nos conectamos al servidor SMTP de Gmail
serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
#serverSMTP.ehlo()
serverSMTP.starttls()
#serverSMTP.ehlo()
serverSMTP.login(user=emisor,password=SENDER_PASS)

#Configuración del mail
mensaje = MIMEText("Este correo ha sido enviado desde Python \
                    wereerewrewrwe \
                    ereerewrewrwere ")

mensaje['From']=emisor
mensaje['To']=receptor
mensaje['Subject']="Mi primer correo desde Python"

""" subject = "Mi primer correo desde Python"
message = "Este correo ha sido enviado desde Python \
                    wereerewrewrwe \
                    ereerewrewrwere "
message = 'Subject: {}\n\n{}'.format(subject, message)
 """

# Enviamos el mensaje
serverSMTP.sendmail(from_addr=emisor,to_addrs=receptor,msg=mensaje.as_string())
#serverSMTP.sendmail(from_addr=emisor,to_addrs=receptor,msg=message)

# Cerramos la conexión
serverSMTP.close()
#serverSMTP.quit()

""" raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials x14sm1495366oiv.39 - gsmtp') 
Solución
https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

I had the same issue. The Authentication Error can be because of your security settings, the 2-step verification for instance. It wont allow third party apps to override the authentication.

Log in to your Google account, and use these links:
Step 1 [Link of Disabling 2-step verification]:

https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin

Step 2: [Link for Allowing less secure apps]

https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none

It should be all good now.

"""