import smtplib #simple mail transfer protocol library
import speech_recognition as sr #speech recognizer
import pyttsx3 #Text to speech

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

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

def  send_mail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('exampleemail@gmail.com', 'examplepass') #Ensure you have your mail in an environment variable for security reason
    server.sendmail(
        'exampleemail@gmail.com', #From
        'exampleemail2@gmail.com', #To
        'Hello, join the party today' #Body

    )

email_list = {
    'dude': 'dude@gmail.com',
    'programming': 'programming@gmail.com',
    'code': 'code@gmail.com',

}

def get_email_info():
    talk('To whom do you want to send the email?')
    name = get_info() #Get input from user
    receiver = email_list[name]
    print('Email recepient: ', receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the message of your email')
    message = get_info()

    send_mail(receiver, subject, message)


get_email_info()
