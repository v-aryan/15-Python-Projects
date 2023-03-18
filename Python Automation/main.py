import schedule
import time
import requests

def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone' : '+447429283885',
        'message' : "Good Morning I am Python",
        'key' : "textbelt"
    })
    print(resp.json())

#schedule.every().day.at('08:03').do(send_message())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
