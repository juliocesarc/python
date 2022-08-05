from datetime import datetime
from locale import setlocale, LC_ALL
import os

from dados_email import EMAIL_ADDRESS, EMAIL_PASSWORD
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import smtplib



# Setando a lingua para de configuração do dispositivo cliente
setlocale(LC_ALL, '')

# Pegando o nome da pasta "aula71"
pasta = os.path.dirname(__file__)

# Obtendo a data atual e formatando-a
data = datetime.now()
data_formatada = data.strftime('%A, %d de %B de %Y')

# Abrindo o arquivo html, lendo com a função Template(),
# e substituindo os caracteres precedidos pelo cifrão "$"
# pelos respectivos valores
with open(f'{pasta}\plate.html', 'r', encoding='utf-8') as file:
    template = Template(file.read())
    corpo_msg = template.safe_substitute(nome='Julio C', data=data_formatada)

# Configurando assunto, quem está enviando e para quem
msg = MIMEMultipart()
msg['subject'] = 'Atenção: este é um e-mail de testes!'
msg['from'] = 'Julio César Costa Silva'
msg['to'] = EMAIL_ADDRESS

# Atribuindo o html lido pela função template e agora já modificado
# ao corpo do email, logo adicionando 'html', para esclarecer.
# Adicionando no escopo do email para finalizar
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# Lendo a imagem e assim como antes feito adicionando no escopo do
# email
with open(f'{pasta}\imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# abrindo conexão com os servidores do gmail, e enviando a porta
# realizando login e enviando a msg
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('Email enviado!')