import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('exampleemail@gmail.com', 'examplepass') #Ensure you have your mail in an environment variable for security reason
server.sendmail(
    'exampleemail@gmail.com', #From
    'exampleemail2@gmail.com', #To
    'Hello, join the party today' #Body

)