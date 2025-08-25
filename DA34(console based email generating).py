#secured mail transfer protocol(smtplib)
#multipurpose intermail extension(mime)
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def otp_generation():
    otp=random.randint(100000,999999)
    return otp
def sending_mail(sender_mail, sender_password, receiver_mail, otp):
    mail=MIMEMultipart()
    mail['To']=receiver_mail
    mail['From']=sender_mail
    mail['Subject']="OTP for verification"

    text=f"Your OTP for verification is {otp}.It is valid for 5 min.Please confirm"
    body=MIMEText(text,'plain')
    mail.attach(body)

    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_mail, sender_password)
    server.send_message(mail)
    server.quit()
    print ("OTP sent successfully")

def otp_verification(otp):
    user_otp=int(input("Enter the otp you receieved: "))
    if user_otp==otp:
        print("OTP verification successful")
    else:
        print("Verification failed")

otp=otp_generation()
sender_mail="daysblike12@gmail.com"
sender_password="msur zgca reke aspu"
receiver_mail=input("Enter receiver mail: ")
sending_mail(sender_mail, sender_password, receiver_mail,otp)
otp_verification(otp)

