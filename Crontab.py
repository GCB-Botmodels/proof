#para guardar una variable y su valor en el entorno
SENDER_PASS = ''

#luego se recupera de este modo
import smtplib
import os
from email.mime.text import MIMEText

emisor = "bot01alerta@gmail.com"
receptor = "cabigerman@gmail.com"

#Nos conectamos al servidor SMTP de Gmail
serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
serverSMTP.ehlo()
serverSMTP.starttls()
serverSMTP.ehlo()
serverSMTP.login(emisor,SENDER_PASS)

#Configuración del mail
mensaje = MIMEText("Este correo ha sido enviado desde Python \
                    wereerewrewrwe \
                    ereerewrewrwere ")

mensaje['From']=emisor
mensaje['To']=receptor
mensaje['Subject']="Mi primer correo desde Python"

# Enviamos el mensaje
serverSMTP.sendmail(emisor,receptor,mensaje.as_string())

# Cerramos la conexión
serverSMTP.close()

