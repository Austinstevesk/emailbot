import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

def get_info():
    try:
        with sr.Microphone() as source: 
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info
            

    except:
        pass

def  send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('exampleemail@gmail.com', 'examplepass') #Ensure you have your mail in an environment variable for security reason
    server.sendmail(
        'exampleemail@gmail.com', #From
        'exampleemail2@gmail.com', #To
        'Hello, join the party today' #Body

    )