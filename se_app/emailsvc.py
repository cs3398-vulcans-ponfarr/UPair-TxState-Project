import smtplib
import config


def send_email(subject, msg, ureciever, usender):
    try:
        if ureciever is None:
            ureciever = 'UPairsvc@gmail.com'
        if subject == 1:
            subject = 'UPair Request from ' + usender
        else:
            subject = 'No subject'
        if msg == 1:
            msg = '<Greetings from UPair! This is an automated message notifying you that you have received a pair ' \
                  'request. The user with email ' + usender + ' shares multiple classes with you! Send them an ' \
                  'email and start a study connection.'
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


#send_email(subject, msg, ureciever)
