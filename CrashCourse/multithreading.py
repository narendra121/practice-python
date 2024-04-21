import threading
import time

results={}

def longTime(num,results):
    time.sleep(1)
    results[num]= num**2
    
t1=threading.Thread(target=longTime,args=(2,results))
t2=threading.Thread(target=longTime,args=(3,results))

t1.start()
t2.start()

t1.join() #pause until succeeded
t2.join()
print(results)


# other way
threads=[threading.Thread(target=longTime,args=(n,results)) for n in range (0,10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)


#multi processing
#pip multi procss
from multiprocess import Process

def longTime(num,results):
    time.sleep(1)
    print( num**2)
    
p1=Process(target=longTime,args=(2,results))
p2=Process(target=longTime,args=(3,results))

p1.start()
p2.start()

p1.join() #pause until succeeded
p2.join()
print(results)