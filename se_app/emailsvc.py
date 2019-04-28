import smtplib
import config


def send_email(subject, msg, ureciever):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, ureciever, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = 'UPair Request'
msg = '<Greetings from UPair! This is an automated message notifying you that you have received a pair request \
       hello from our college class matching service. Should you wish to accept this request, please follow the \
       following link if you wish to accept: http://127.0.0.1:5000/'
ureciever = 'UPairsvc@gmail.com'

send_email(subject,msg,ureciever)
