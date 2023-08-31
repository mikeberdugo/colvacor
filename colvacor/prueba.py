import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos del remitente
remitente = 'Notificaciones_colvacor@hotmail.com'
contraseña = 'Bogota.30'

# Datos del destinatario
destinatario = 'manuel.david.13.b@gmail.com'

# Configurar el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = 'prueba'

cuerpo = 'estas mal '

mensaje.attach(MIMEText(cuerpo, 'plain'))

# Conectar y enviar el correo
try:
    servidor = smtplib.SMTP('smtp.live.com', 25)  # Para Hotmail/Outlook
    servidor.starttls()
    servidor.login(remitente, contraseña)
    servidor.sendmail(remitente, destinatario, mensaje.as_string())
    servidor.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print("Error al enviar el correo:", str(e))
