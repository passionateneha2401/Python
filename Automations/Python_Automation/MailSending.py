################################################################
# Program: Simple Gmail Mail Sender
# Author : Neha Vilas Kumbhar
# Purpose: Send mail using Python SMTP
#################################################################
import smtplib
from email.message import EmailMessage

###############################################
#Function : Marvellous_send_mail
#Description : Sends email using Gmail SMTP server
################################################

def send_mail(sender,app_password,receiver,subject,body):
    #create email object
    msg = EmailMessage()

    #set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #add mail body
    msg.set_content(body)

    #create smtp ssl connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    #login using gmail + app password
    smtp.login(sender,app_password)

    #send the mail
    smtp.send_message(msg)

    #close connection
    smtp.quit()

###############################################################
# Function : main
# Description : Driver Code
###############################################################

def main():

    #always use seperate temporary/testing account
    sender_email = "demon10feb@gmail.com"

    #app password generated from google account
    app_password = "pvsbvsizjroxrpfy"

    #your second email for testing
    receiver_emial = "itsneha2024@gmail.com"

    subject = "Test Mail from Python script"

    body = '''Jay Ganesh,
    This is a test email sent using Marvellous Python.

    Regards,
    Marvellous Infosystems
    '''

    send_mail(sender_email,app_password,receiver_emial,subject,body)

    print("Marvellous mail Sent Successfully")

###########################################################
# Program Entry POint
#############################################################

if __name__ == "__main__":
    main()

