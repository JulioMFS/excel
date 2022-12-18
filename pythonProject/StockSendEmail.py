import requests
import smtplib
import time
import os

api_key = 'dd1932a45e23aa5c21f38f9e9b10403b'
password = 'Julio301052'
cstr = "  Apple & FaceBook Stock values  "
#print(f'Hello, {os.getlogin()}! How are you?\n\tApple:\t{aaplstockPrice}\tFaceBook: {fbstockPrice}')
print (cstr.center(40, '#'))
def send_mail(password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanfonaj@gmail.com', password)
    subject = 'test'
    body = 'price down'

    msg = f'subject: {subject} {body}'

    server.sendmail(
        'jsanfona@gmail.com',
        'jsanfona@gmail.com',
        msg
    )
    print('email is sent')
    server.quit()


def price_tracker(api_key, password):
    aaplprices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key}').json()
    fbprices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/FB?apikey={api_key}').json()

    aaplstockPrice = aaplprices[0]['price']
    fbstockPrice = fbprices[0]['price']
    #print(aaplstockPrice)
    #print(fbstockPrice)

    print(f'Apple:\t{aaplstockPrice}\tFaceBook: {fbstockPrice}')
    if aaplstockPrice < 140 and fbstockPrice < 320:
        send_mail(password)


# run evrey 10 minutes
while (True):
    price_tracker(api_key, password)
    time.sleep(10)