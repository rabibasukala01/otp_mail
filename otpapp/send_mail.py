import smtplib
from email.message import EmailMessage


def send_mail(otpAsMessage):

    # Creditials
    sender = 'pytest578@gmail.com'
    password = 'evyzestqxyfzhngm'
    receiver = 'rabibasukala16@gmail.com'

    # creating email format:
    message = EmailMessage()
    message['Subject'] = "smptlib with EmailMessage"
    message['From'] = sender
    message['To'] = receiver
    body = f'<h1>{otpAsMessage}</h1>'

    # no need subtype for plain text
    message.set_content(body, subtype='html')

    # creating smtp object
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # tts-transfer layer security improved version of ssl
    server.starttls()
    # login with google app password since less secure app of google discontinue fom may 30 2022
    server.login(sender, password)
    # sending mail to target
    server.send_message(message)
    # quiting session
    server.quit()

    print("Successfully sent")
