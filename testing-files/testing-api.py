import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

bot_token = '1840792617:AAF1VbewS72xizg1fl6DjgK40p40i6NVTBo'
chat_id = '-1001460807540'

def send_to_telega(bot_token, chat_id, message):
    print (bot_token, chat_id, message)
    url = (f'''https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}''')
    response = requests.get(url)



fail = False
failed = 0

#the First api test
url = "http://3.121.127.141/result"
response1 = requests.get(url)

print ("the first test's result is -", response1)
if response1.status_code != 200:
    fail = True
    failed +=1

#the second api test
url = "http://3.121.127.141/create_record"
data = {"create_name": "test", "create_desc": "test", "create_number": 1, "create_price": 1, "create_rare": "N"}

response2 = requests.post(url, data=data)

print ("the second test's result is -", response2)
if response2.status_code != 200:
    fail = True
    failed +=1



#the third api test
url = "http://3.121.127.141/n_record"
data = {"send_n": 1}
response3 = requests.post(url, data=data)

print ("the third test's result is -", response3)
if response3.status_code != 200:
    fail = True
    failed +=1

soup = BeautifulSoup(response3.content, "lxml")
result = soup.find('p',text=re.compile('rare'))
id = result.text.replace('rare','').strip()[60:].split()[0]



#the fourth api test
url = "http://3.121.127.141/id_record"
data = {"send_id": id}
response4 = requests.post(url, data=data)

print ("the fourth test's result is -", response4)
if response4.status_code != 200:
    fail = True
    failed +=1



#the fifth api test
url = "http://3.121.127.141/delete_id"
data = {"send_del_id": id}
response5 = requests.post(url, data=data)

print ("the fifth test's result is -", response5)
if response5.status_code != 200:
    fail = True
    failed +=1


print ("there was created and deleted record with id -", id)
print ()

message = ''
curent_time = datetime.now().strftime("_%d.%m.%Y_%H.%M")
if fail == True:
    message = f'''API-Testing Failed ! Failed: {failed}. Passed: {5-failed}. Deploy canceled. Time of build: {curent_time}.'''
else:
    message = "API-Testing is successesful. All tests are passed. Code is ready for the next step!"
    os.system("cp /home/ubuntu/fromgit/artifact.tar.bz2 /home/ubuntu/after-testing")

send_to_telega(bot_token, chat_id, message)

