import re
import paramiko
import time
BUF_SIZE = 20000
TIMEOUT = 1

def terminal(command: str):
    # Создаем объект — соединение по ssh
    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    login, pwd = 'restapi', 'j0sg1280-7@'

    # Инициируем соединение по ssh
    ssh_connection.connect('10.31.70.209', username=login, password=pwd, look_for_keys=False, allow_agent=False)
    session = ssh_connection.invoke_shell()
    session.send("\n")

    session.recv(BUF_SIZE)
    session.send("terminal length 0\n")
    time.sleep(TIMEOUT)

    session.send("\n")
    res = session.recv(BUF_SIZE)
    session.send(f'{command}\n')
    time.sleep(TIMEOUT*2)

    s = session.recv(BUF_SIZE).decode()
    session.close()
    return s


portyanka = terminal('show interface')

'''
re.match()

Структура:

GigabitEthernet1 is up, line protocol is up 
^-name:  r'(*) is up'
...
10532706 packets input, 769078236 bytes, 0 no buffer
^-input
...
119711 packets output, 43112989 bytes, 0 underruns
^-output
'''


# All output
# print(portyanka)


Int = re.finditer(r'([A-Za-z]{1,100}[0-9]{1,5}) is', portyanka)
for x in Int:
    print(x.group(1))

print('\n')
In = re.finditer(r'([0-9]{1,16}) packets input, ([0-9]{1,16}) bytes', portyanka)
for x in In:
    print(f'INPUT | packets: {x.group(1)}, bytes:{x.group(2)}')

print('\n')
Out = re.finditer(r'([0-9]{1,16}) packets output, ([0-9]{1,16}) bytes', portyanka)
for x in Out:
    print(f'OUT | packets: {x.group(1)}, bytes:{x.group(2)}')

