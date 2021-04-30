import smtplib

smtp_server = 'smtp.gmail.com'
port = 465
server = smtplib.SMTP_SSL(smtp_server, port)
sender = input("Enter your gmail address: ")
password = input("Enter your password: ")

def server_connection():
   try:
      server.ehlo()
      server.login(sender, password)
      print("Successful login!")
      send_email()
   except Exception as e:
      print(e, "\nSomething went wrong: *Login failed*")

def send_email():
   try:
      recipient = input("Enter recipient email: ")
      message = input("Enter message: ")
      server.sendmail(sender, recipient, message)
      server.close()
      print("Email has been sent!")
   except Exception as e:
      print(e, "\nSomething went wrong: *Email could not be sent*")
      send_email()

server_connection()







