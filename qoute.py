import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def getquote():
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)
    js = response.json()
    quote = js["quote"]["body"]
    author = js["quote"]["author"]
    whole = quote + " - " + author
    return whole

def sendquote():
    msg = getquote()
    send = MIMEMultipart()
    send['From'] = "abc@xxx.com"
    send['To'] =  "def@xxx.com"
    send['Subject'] = "A Quote A Day"
    body = msg+"\n\n\n\n\n\n\nNote: Its an automated script, let me know for changes or suggestions"
    send.attach(MIMEText(body, 'plain'))
    text = send.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sendermail@domain.com", "password")
    server.sendmail("sendermail@domain.com", "receivermail@domain.com", text)
    server.quit()


def main():
    sendquote()

if __name__ == "__main__":
    main()
