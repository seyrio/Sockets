# import nmap
# begin = 75
# end = 80
# target = '127.0.0.1'
# scanner = nmap.PortScanner()
# for i in range(begin, end+1):
#     res = scanner.scan(target,str(i))
#     res = res['scan'][target]['tcp'][i]['state']
#     print(f'port {i} is {res}.')

from socket import *
import time

startTime = time.time()

if __name__ == "__main__":
    target = input('enter host for scanning: ')
    t_ip = gethostbyname(target)
    print('starting scanning on host: ', t_ip)

    for i in range(50,100):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_ip,i))
        if conn==0:
            print(f'port {i} is open')
        else: 
            print(f'port {i} is closed')
        s.close()
    
print("time taken", time.time()-startTime)