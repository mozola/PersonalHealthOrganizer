# -*- coding: utf-8 -*-
import smtplib

TO = 'mozola.waldemar@gmail.com'                            #please write TO email
SUBJECT = 'Lista zakupow na sprint'
TEXT ='Poniżej znajduje się lista zakupów na najbliższy sprint \r'

SENDER = 'mozola.waldemar@gmail.com'      #please write your email
PASSWORD = 'atb7jwnd'                       #please write your password to email

FOTTER = "\rPozdrawiam, \r Program DIX \r Ta wiadomosc zostala wyslana automatycznie."

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo
server.login(SENDER, PASSWORD)


msg = "\r\n".join([
  "From: {}",
  "To: user_you@gmail.com",
  "Subject: Lista zakupow na sprint",
  "",
  "{}"
  ])


def generate_msg(components):
    components_list = []
    components_list.append(TEXT)

    for key, value in components.iteritems():
        components_list.append('{} \r{}'.format(key, value))
    components_list.append(FOTTER)

    return '\n'.join(components_list)



def send_main(msga):
    try:
        server.sendmail(SENDER, TO , msg.format(SUBJECT, generate_msg(msga)))
        print 'SUCCES: Mail was sended'
    except:
        print 'ERROR: Mail not sended'

    server.quit()