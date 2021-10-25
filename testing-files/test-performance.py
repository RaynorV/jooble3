import subprocess
import requests

bot_token = '1840792617:AAF1VbewS72xizg1fl6DjgK40p40i6NVTBo'
chat_id = '-1001460807540'

def send_to_telega(bot_token, chat_id, message):
    print (bot_token, chat_id, message)
    url = (f'''https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}''')
    response = requests.get(url)


m = 21  #normal average response time
m5percent = (5*m)/100    #canculating 5% of m (normal average response time)

command = "/home/ubuntu/jmiter/apache-jmeter-5.4.1/bin/jmeter.sh -n -t /home/ubuntu/jmiter/5minuteSummary-Report.jmx -l /home/ubuntu/jmiter/logfile.log"
s1 = subprocess.check_output(command, shell=True)  #getting result of performance test
print ('Result (all) is --------------------------\n', s1)

avg = int(s1[-133:-120].split()[1])  #getting one number from output (curent averege response time)

print ('\nAverage response time is - ', avg)

message = ""
if (avg - m)  > m5percent:
    message = '''Performance test failed ! Average response time is{avg}. But epected - is {m}. Deploy CANCELED :( '''
else:
    message = "Performanse testing finished. Everything is fine. Average response time is normal"


send_to_telega(bot_token, chat_id, message)

