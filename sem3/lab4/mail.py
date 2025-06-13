import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from secrets import myUser, myPassword

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

server.login(myUser, myPassword)

msg = MIMEMultipart()
msg['From'] = 'pe.pavlenko@mail.ru'
msg['To'] = 'pavlnkopavel@gmail.com'
msg['Subject'] = 'Test Email'

# Добавление текста в письмо
body = "This is a test email message."
msg.attach(MIMEText(body, 'plain'))

# Добавление фотографии в письмо
with open("image.jpg", 'rb') as f:
    img = MIMEImage(f.read())
msg.attach(img)

# Добавление файла в письмо
with open("test.pdf", 'rb') as file:
    pdf = MIMEBase('application', 'octet-stream', Name='test.pdf')
    pdf.set_payload(file.read())
encoders.encode_base64(pdf)
pdf.add_header('Content-Disposition', "attachment; filename= %s" % 'test.pdf')
msg.attach(pdf)

# Отправка письма
text = msg.as_string()
server.sendmail(msg['From'], msg['To'], text)
print("Письмо отправлено успешно")



