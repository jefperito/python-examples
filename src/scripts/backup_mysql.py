# -*- coding: utf-8 -*-
import sys, os, time
from datetime import datetime

def getTime():
    now = datetime.today() #2012-02-02 12:18:18.153000
    now = str(now).replace(' ', '_') #2012-02-02_12:18:18.153000
    now = now.replace(':', '-') #2012-02-02_12-18-18.153000
    
    return now.split('.')[0] #2012-02-02_12-18-18

def loop(username, password, database):
    while True:
        now = getTime()

        os.system('mysqldump -u ' + username + ' -p' + password + ' ' + database + ' > backup_' + now + '.sql')
        
        time.sleep(3600) #Durma por uma hora

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit('Quantidade de parâmetros inválidos')

    loop(sys.argv[1], sys.argv[2], sys.argv[3])