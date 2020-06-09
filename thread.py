import threading
import time# 子執行緒，也就是你第二個需要執行的程式

'''
time.sleep(2)

def job_2():
	print('thread %s is running...' % threading.current_thread().name)
	for i in range(5):
		print("-----second program------:", i)
		time.sleep(2)
# 設定子執行緒
t = threading.Thread(target = job_2)# 執行他
t.start()
print('first thread %s is running...' % threading.current_thread().name) # 現在運行的程序名稱
print("threading.active_count():",threading.active_count())
#print("threading.enumerate():",threading.enumerate())

# 這邊開始寫你主要程式碼的工作


for i in range(2):
	print("------main program-------:", i)
	time.sleep(1)
    
#t.join()
print('thread %s is running...' % threading.current_thread().name)
print("Done.")
'''
#-------------------------------------------------------------------------------------
'''
import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(10000000))
    #print(l)
    s_t = time.time()
    normal(l*4)
    
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
'''
#----------------------------------------------

#print("-----------------------------------------------------")

import requests
import time



url = 'https://www.google.com.tw/'

#start_time = time.time()

def send_req(url):
    
    t = time.time()
    print("Send a request")#,t-start_time,"seconds.")

    res = requests.get(url)

    t = time.time()
    print("Receive a response")#,t-start_time,"seconds.")
    
    
start_time = time.time()
for i in range(10):
    
    send_req(url)
stop_time= time.time()

print("total_time_sync:",stop_time-start_time)


print("-----------------------------------------------------")


import requests
import time
import asyncio

url = 'https://www.google.com.tw/'
loop = asyncio.get_event_loop()





async def send_req(url,total):
    t = time.time()
    print("Send a request")#,t-start_time,"seconds.")
    #start_time = time.time()
    res = await loop.run_in_executor(None,requests.get,url)
    t = time.time()
    print("Receive a response")#,t-start_time,"seconds.")

start_time = time.time()
tasks = []
for i in range(10):
    
    task = loop.create_task(send_req(url,0))
    
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
stop_time= time.time()
print("total_time_async:",stop_time-start_time)
