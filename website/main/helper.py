from flask_mail import Message
import os
from website import mail


def send_contact_email(name, email, message):    
   msg=Message(subject='Contuct us request',
               sender= os.environ.get('EMAIL_USER'),
               recipients= [os.environ.get('EMAIL_USER')],
               body=
            f'''
                New Message Received!
                Name:{name}
                Email: {email}
                Message:
    
                    {message}    
                '''
              )
   mail.send(msg)